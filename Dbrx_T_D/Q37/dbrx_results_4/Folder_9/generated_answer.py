def filter_chars(s):
    res = ''
    for i in range(len(s)):
        if not (38 <= i <= 99 and s[i].isalpha() and ('A' <= s[i] <= 'Q')):
            res += s[i]
    return res