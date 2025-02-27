def filter_chars(s):
    chars_to_filter = [s[i] for i in range(46, 91)]
    for c in chars_to_filter:
        if 'D' < c < 'H':
            s = ''.join((ch for ch in s if ch != c))
    return s