def remove_repeat_chars(s):
    chars = {}
    for i in range(200, 203):
        if i < len(s):
            if s[i] in chars:
                chars[s[i]] += 1
            else:
                chars[s[i]] = 1
    for c in chars:
        if chars[c] > 1:
            s = ''.join([x for x in s if x != c])
    return s