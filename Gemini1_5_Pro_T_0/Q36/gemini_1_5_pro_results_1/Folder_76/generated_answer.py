def filter_chars(s):
    t = ''
    for i in range(len(s)):
        if 669 <= i <= 888 and 'B' < s[i] < 'Y':
            continue
        t += s[i]
    return t