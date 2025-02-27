def filter_chars(s):
    chars_to_filter = set()
    for i in range(45, 59):
        if '/' < s[i] < '6':
            chars_to_filter.add(s[i])
    return ''.join((c for c in s if c not in chars_to_filter))