def filter_chars(s):
    new_s = ''
    for i in range(len(s)):
        if i <= 21 or i >= 43:
            new_s += s[i]
    new_s = ''.join((c for c in new_s if c < '+' or c > '8'))
    return new_s