def filter_chars(s):
    for i in range(len(s)):
        if i < 3 and '$' < s[i] < '?':
            s = s.replace(s[i], '')
    return s