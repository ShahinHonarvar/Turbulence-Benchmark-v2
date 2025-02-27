def filter_chars(s):
    chars_to_remove = [c for c in s if 1 <= s.index(c) <= 7 and 'L' <= c <= 'a']
    for c in chars_to_remove:
        s = s.replace(c, '', 1)
    return s