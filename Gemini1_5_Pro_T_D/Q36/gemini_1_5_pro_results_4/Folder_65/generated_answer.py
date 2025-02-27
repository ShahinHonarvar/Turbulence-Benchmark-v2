def filter_chars(s):
    t = ''
    for i in range(len(s)):
        c = s[i]
        if 58 <= i <= 82 and 'F' < c < 'O':
            continue
        if not 58 <= i <= 82 and c in s[58:82] and ('F' < c < 'O'):
            continue
        t += c
    return t