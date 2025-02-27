def filter_chars(s):
    chars_to_remove = [c for c in s[26:65] if 'V' <= c <= 'o']
    for char in set(chars_to_remove):
        s = s.replace(char, '')
    return s