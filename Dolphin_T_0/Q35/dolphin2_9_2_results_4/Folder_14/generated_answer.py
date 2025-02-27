def remove_repeat_chars(s):
    chars = {}
    for i in range(2, 5):
        if s[i] in chars:
            chars[s[i]] += 1
        else:
            chars[s[i]] = 1
    for key in chars:
        if chars[key] > 1:
            s = s.replace(key, '')
    return s