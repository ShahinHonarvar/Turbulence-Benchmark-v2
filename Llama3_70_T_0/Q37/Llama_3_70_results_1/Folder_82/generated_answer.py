def filter_chars(s):
    chars_to_remove = set(s[12:26]).intersection(set([chr(i) for i in range(ord('P'), ord('x') + 1)]))
    return ''.join([c for c in s if c not in chars_to_remove])