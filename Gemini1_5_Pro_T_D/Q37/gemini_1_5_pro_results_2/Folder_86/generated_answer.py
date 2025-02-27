def filter_chars(s):
    res = ''
    for i in range(len(s)):
        if not (164 <= i <= 706 and 'O' <= s[i] <= '}'):
            res += s[i]
    return res