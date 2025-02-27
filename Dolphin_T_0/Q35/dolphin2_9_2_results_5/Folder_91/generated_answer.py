def remove_repeat_chars(s):
    for i in range(7):
        for j in range(i + 2, 7):
            if s[i] == s[j]:
                s = s.replace(s[i], '')
    return s