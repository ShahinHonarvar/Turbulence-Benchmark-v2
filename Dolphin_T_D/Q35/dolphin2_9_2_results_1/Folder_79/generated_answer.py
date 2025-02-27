def remove_repeat_chars(s):
    chars = {}
    for i in range(1, 7):
        if s[i] not in chars:
            chars[s[i]] = 1
        else:
            chars[s[i]] += 1
    new_s = ''
    for c in s:
        if chars.get(c) == 1:
            new_s += c
    return new_s