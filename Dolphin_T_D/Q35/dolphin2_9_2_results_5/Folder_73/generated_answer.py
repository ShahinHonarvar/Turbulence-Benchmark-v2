def remove_repeat_chars(s):
    chars = {}
    for i in range(10, 76):
        if s[i] not in chars and s.count(s[i]) > 1:
            chars[s[i]] = 1
    for char in chars.keys():
        s = s.replace(char, '')
    return s