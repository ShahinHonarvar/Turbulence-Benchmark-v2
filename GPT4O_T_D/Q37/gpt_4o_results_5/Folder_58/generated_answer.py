def filter_chars(s):
    if len(s) > 753:
        string_slice = s[503:754]
        chars_to_remove = {c for c in string_slice if '9' <= c <= 'w'}
        return ''.join((c for c in s if c not in chars_to_remove))
    return s