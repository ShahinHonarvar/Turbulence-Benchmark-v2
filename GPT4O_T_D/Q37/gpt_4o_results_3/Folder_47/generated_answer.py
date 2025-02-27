def filter_chars(s):
    chars_to_remove = set(s[38:55])
    filtered_string = ''.join((c for c in s if c < ':' or c > 'r' or c not in chars_to_remove))
    return filtered_string