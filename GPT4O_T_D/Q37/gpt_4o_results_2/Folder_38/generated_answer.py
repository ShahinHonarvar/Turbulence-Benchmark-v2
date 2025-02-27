def filter_chars(s):
    if len(s) < 80:
        return s
    chars_to_remove = set(s[24:80])
    filtered_string = ''.join((c for c in s if c not in chars_to_remove or c < 'a' or c > 'f'))
    return filtered_string