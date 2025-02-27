def filter_chars(s):
    for i in range(72, 95):
        for j in range(len(s) - 1, -1, -1):
            if ord(s[j]) == i and ord('.') <= i <= ord('b'):
                s = s[:j] + s[j + 1:]
    return s