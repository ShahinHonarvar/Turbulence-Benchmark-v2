def filter_chars(s):
    chars_to_remove = set(filter(lambda c: 'D' <= c <= 'u', s[227:236]))
    return ''.join((c for c in s if c not in chars_to_remove))