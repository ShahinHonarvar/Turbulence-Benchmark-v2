def remove_repeat_chars(s):
    repeated_chars = []
    for i in range(91, 97):
        for j in range(i + 1, 97):
            if s[i] == s[j] and s[i] not in repeated_chars:
                repeated_chars.append(s[i])
    for char in repeated_chars:
        s = s.replace(char, '')
    return s