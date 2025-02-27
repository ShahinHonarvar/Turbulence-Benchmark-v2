def filter_chars(s):
    for i in range(1, 7):
        for j in range(i, len(s)):
            c = s[j]
            if c > '3' and c < '^':
                s = s[:j] + s[j + 1:]
        return s