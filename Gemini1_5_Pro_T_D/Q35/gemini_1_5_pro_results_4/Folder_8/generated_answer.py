def remove_repeat_chars(s):
    repeated_chars = set()
    for i in range(46, 48):
        if s[i] in s[46:48] and s[i] not in repeated_chars:
            repeated_chars.add(s[i])
    for char in repeated_chars:
        s = s.replace(char, '')
    return s