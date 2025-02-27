def filter_chars(s):
    exclude_range = s[25:37]
    chars_to_exclude = {c for c in exclude_range if 'A' < c < 'h'}
    filtered_string = ''.join((c for c in s if c not in chars_to_exclude))
    return filtered_string