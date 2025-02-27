def filter_chars(s):
    chars_to_remove = [c for c in s if 42 <= s.index(c) <= 92 and '/' <= c <= 'a']
    for char in chars_to_remove:
        s = s.replace(char, '', 1)
    return s