def filter_chars(s):
    chars_to_filter = set((c for c in s if 42 <= ord(c) <= 97 and '*' <= c <= 'b'))
    return ''.join((c for c in s if c not in chars_to_filter))