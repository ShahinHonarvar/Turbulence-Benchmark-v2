def filter_chars(s):
    chars_to_remove = set(s[71:95])
    altered_string = ''.join((c for c in s if c not in chars_to_remove or c < 'K' or c > 'a'))
    return altered_string