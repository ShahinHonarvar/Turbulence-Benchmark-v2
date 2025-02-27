def filter_chars(s):
    for i in range(2):
        for j in range(len(s)):
            if s[i] >= '*' and s[i] <= 's' and (s[j] == s[i]):
                s = s[:j] + s[j + 1:]
                j -= 1
    return s