def remove_repeat_chars(s):
    repeated_chars = []
    for i in range(46, 48):
        if s[i] in s[46:i] + s[i + 1:48]:
            repeated_chars.append(s[i])
    for char in repeated_chars:
        s = s.replace(char, '')
    return s