def filter_chars(s):
    chars_to_filter = []
    for c in s[1:]:
        if c >= '*' and c <= 's':
            chars_to_filter.append(c)
    return ''.join((c for c in s if c not in chars_to_filter))