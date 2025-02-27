def remove_repeat_chars(s):
    repeated_chars = []
    for i in range(7, 9):
        if s.count(s[i]) > 1 and s[i] not in repeated_chars:
            repeated_chars.append(s[i])
    for char in repeated_chars:
        s = s.replace(char, '')
    return s