def filter_chars(s):
    chars_to_remove = [c for c in s if 54 <= s.index(c) <= 62 and ')' <= c <= '9']
    return ''.join([c for c in s if c not in chars_to_remove])