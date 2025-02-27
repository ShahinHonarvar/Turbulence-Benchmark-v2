def filter_chars(s):
    t = ''
    for i in range(len(s)):
        if not (38 <= i <= 69 and 'H' <= s[i] <= 'e'):
            t += s[i]
    return t