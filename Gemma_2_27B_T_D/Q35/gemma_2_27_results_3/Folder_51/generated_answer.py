def remove_repeat_chars(s):
    repeat_chars = {}
    for i in range(6, 9):
        if s[i] in repeat_chars:
            repeat_chars[s[i]] += 1
        else:
            repeat_chars[s[i]] = 1
    for char, count in repeat_chars.items():
        if count > 1:
            s = s.replace(char, '')
    return s