def filter_chars(s):
    chars_to_remove = set(s[220:403])
    filtered_chars = ''.join((c for c in s if c not in chars_to_remove if '*' < c < '7'))
    return filtered_chars