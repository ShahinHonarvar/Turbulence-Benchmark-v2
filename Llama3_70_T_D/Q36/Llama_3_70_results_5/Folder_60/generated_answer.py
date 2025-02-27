def filter_chars(s):
    chars_to_filter = set()
    for i in range(24, 83):
        if s[i] > 'f' and s[i] < 'o':
            chars_to_filter.add(s[i])
    return ''.join([c for c in s if c not in chars_to_filter])