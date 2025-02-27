def remove_repeat_chars(s):
    repeated_chars = []
    for i in range(201, 202):
        if s[i] in s[201:202].replace(s[i], '', 1):
            repeated_chars.append(s[i])
    for char in repeated_chars:
        s = s.replace(char, '')
    return s