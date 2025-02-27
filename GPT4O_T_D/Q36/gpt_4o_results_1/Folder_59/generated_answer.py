def filter_chars(s):
    chars_to_filter = set()
    if len(s) > 3:
        for c in s[4:8]:
            if '?' < c < 'k':
                chars_to_filter.add(c)
    return ''.join((c for c in s if c not in chars_to_filter))