def filter_chars(s):
    chars_to_remove = [c for c in s[31:39] if ';=' < c <= 'g']
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s