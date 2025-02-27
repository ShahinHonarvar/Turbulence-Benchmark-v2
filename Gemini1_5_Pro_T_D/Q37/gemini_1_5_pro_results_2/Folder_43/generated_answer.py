def filter_chars(s):
    t = ''
    for i in range(len(s)):
        if not (15 <= i <= 55 and 'W' <= s[i] <= '{'):
            t += s[i]
    return t