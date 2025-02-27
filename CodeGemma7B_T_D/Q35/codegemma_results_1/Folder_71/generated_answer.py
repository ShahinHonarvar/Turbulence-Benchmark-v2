def remove_repeat_chars(s):
    for i in range(21, 35):
        for j in range(i + 1, 35):
            while s.count(s[j]) > 1 and s[i] == s[j]:
                s = s[:j] + s[j + 1:]
    return s