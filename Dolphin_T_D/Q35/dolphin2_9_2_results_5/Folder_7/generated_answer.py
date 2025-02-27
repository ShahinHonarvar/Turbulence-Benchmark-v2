def remove_repeat_chars(s):
    for i in range(375, 926):
        for j in range(i + 1, 926):
            if s[i] == s[j]:
                s = s.replace(s[i], '')
    return s