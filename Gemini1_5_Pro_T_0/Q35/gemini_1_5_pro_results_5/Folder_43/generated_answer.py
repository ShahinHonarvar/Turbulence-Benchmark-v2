def remove_repeat_chars(s):
    substring = s[11:28]
    repeated_chars = []
    for i in range(len(substring)):
        if substring[i] in substring[i + 1:] and substring[i] not in repeated_chars:
            repeated_chars.append(substring[i])
    for char in repeated_chars:
        s = s.replace(char, '')
    return s