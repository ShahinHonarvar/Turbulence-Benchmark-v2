def filter_chars(s):
    if len(s) <= 83:
        return s
    chars_to_remove = s[83:100]
    chars_set = set((c for c in chars_to_remove if '*' <= c <= 'j'))
    return ''.join((c for c in s if c not in chars_set))