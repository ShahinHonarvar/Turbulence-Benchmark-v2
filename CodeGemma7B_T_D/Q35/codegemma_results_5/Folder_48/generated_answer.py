def remove_repeat_chars(s):
    for i in range(409, 502):
        for j in range(i + 1, 502):
            if s[i] == s[j] and s[i] in s[408:502]:
                for k in range(502, len(s)):
                    if s[k] == s[i]:
                        s = s[:k] + s[k + 1:]
    return s