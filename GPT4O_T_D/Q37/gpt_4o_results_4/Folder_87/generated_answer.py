def filter_chars(s):
    to_remove = set(s[18:82])
    filtered_string = ''.join((c for c in s if not ('W' <= c <= '[' and c in to_remove)))
    return filtered_string