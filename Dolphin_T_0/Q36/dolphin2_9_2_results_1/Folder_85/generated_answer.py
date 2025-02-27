def filter_chars(s):
    s = list(s)
    for c in range(55, 80):
        if s[c] > 'S' and s[c] < 's':
            s = [char for char in s if char != s[c]]
    return ''.join(s)