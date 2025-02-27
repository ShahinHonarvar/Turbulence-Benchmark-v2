def remove_repeat_chars(s):
    repeated_chars = []
    for i in range(57, 84):
        if s[i] in s[57:i] and s[i] not in repeated_chars:
            repeated_chars.append(s[i])
    for char in repeated_chars:
        s = s.replace(char, '')
    return s