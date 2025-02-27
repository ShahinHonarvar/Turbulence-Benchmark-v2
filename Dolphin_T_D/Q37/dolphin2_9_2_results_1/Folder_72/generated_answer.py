def filter_chars(s):
    s = list(s)
    for i in range(35, 52):
        if 'H' <= s[i] <= 's':
            s = [c for c in s if c != s[i]]
    return ''.join(s)