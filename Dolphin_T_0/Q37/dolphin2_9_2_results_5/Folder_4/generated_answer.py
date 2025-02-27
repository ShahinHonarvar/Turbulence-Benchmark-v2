def filter_chars(s):
    chars = [s[i] for i in range(19, 34) if s[i] >= 'S' and s[i] <= '}']
    s = ''.join([c for c in s if c not in chars])
    return s