def remove_repeat_chars(s):
    repeated_chars = []
    for i in range(1, 5):
        for j in range(i + 1, 6):
            if s[i] == s[j] and s[i] not in repeated_chars:
                repeated_chars.append(s[i])
    for c in repeated_chars:
        s = s.replace(c, '')
    return s