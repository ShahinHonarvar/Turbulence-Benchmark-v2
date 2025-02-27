def filter_chars(s):
    chars_to_remove = [c for c in s if 4 <= s.index(c) <= 4 and '7' <= c <= 'o']
    return ''.join((c for c in s if c not in chars_to_remove))