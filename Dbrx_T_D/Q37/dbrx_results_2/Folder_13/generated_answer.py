def filter_chars(s):
    for i in range(len(s)):
        if 124 <= i <= 854 and '9' <= s[i] <= 's':
            s = s[:i] + s[i + 1:]
    return s