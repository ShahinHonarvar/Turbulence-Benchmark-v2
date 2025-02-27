def filter_chars(s):
    res = ''
    for i in range(len(s)):
        if not (35 <= i <= 89 and 'E' <= s[i] <= 't' and (s[i] in s[35:90])):
            res += s[i]
    return res