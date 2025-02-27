def filter_chars(s):
    for c in range(672, 709):
        if s[c] > 'X' and s[c] < '}':
            s = ''.join(filter(lambda x: x != s[c], s))
    return s