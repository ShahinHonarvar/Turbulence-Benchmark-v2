def filter_chars(s):
    t = ''
    for i in range(len(s)):
        if 323 <= i <= 525 and s[i] > ')' and (s[i] < 'O'):
            continue
        t += s[i]
    return t