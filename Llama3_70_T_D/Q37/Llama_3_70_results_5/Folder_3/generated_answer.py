def filter_chars(s):
    chars_to_filter = set(s[37:57]).intersection(set([chr(i) for i in range(ord('6'), ord('_') + 1)]))
    return ''.join([c for c in s if c not in chars_to_filter])