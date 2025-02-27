def remove_repeat_chars(s):
    for i in range(200, 202):
        while i < len(s) and s[i] == s[i - 2] and (s[i] != s[i + 1]):
            s = s[:i] + s[i + 1:]
    return s