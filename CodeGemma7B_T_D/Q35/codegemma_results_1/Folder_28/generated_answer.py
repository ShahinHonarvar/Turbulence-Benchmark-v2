def remove_repeat_chars(s):
    for i in range(86, 99):
        for j in range(i + 1, len(s)):
            if s[i] == s[j]:
                s = s[:i] + s[i + 1:]
    return s