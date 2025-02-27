def remove_repeat_chars(s):
    for i in range(2, 7):
        for j in range(i + 1, 7):
            if s[i] == s[j]:
                while s[j] == s[i]:
                    s = s[:j] + s[j + 1:]
    return s