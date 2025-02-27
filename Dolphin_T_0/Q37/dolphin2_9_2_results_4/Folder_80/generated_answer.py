def filter_chars(s):
    chars_to_remove = [c for c in s[36:80] if 'a' <= c <= 'i']
    for c in set(chars_to_remove):
        s = s.replace(c, '')
    return s