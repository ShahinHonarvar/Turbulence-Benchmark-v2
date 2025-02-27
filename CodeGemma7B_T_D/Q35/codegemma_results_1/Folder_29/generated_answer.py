def remove_repeat_chars(s):
    for i in range(70, 98):
        for j in range(i + 1, 99):
            if s[j] == s[i]:
                s = s[:i] + s[i + 1:]
    return s