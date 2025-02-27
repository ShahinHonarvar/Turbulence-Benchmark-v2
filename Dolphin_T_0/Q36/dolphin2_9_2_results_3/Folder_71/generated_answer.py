def filter_chars(s):
    for c in range(82, 89):
        if s[c] > '*' and s[c] < '[':
            s = ''.join([ch for ch in s if ch != s[c]])
    return s