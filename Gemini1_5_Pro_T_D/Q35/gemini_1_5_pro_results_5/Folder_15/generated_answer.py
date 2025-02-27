def remove_repeat_chars(s):
    for i in range(1, 4):
        for j in range(i):
            if s[i] == s[j]:
                return remove_repeat_chars(s[:i] + s[i + 1:])
    return s