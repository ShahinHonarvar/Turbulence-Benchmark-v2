def remove_repeat_chars(s):
    for i in range(39, 43):
        for j in range(i + 1, 43):
            if s[i] == s[j]:
                s = s.replace(s[i], '')
    return s