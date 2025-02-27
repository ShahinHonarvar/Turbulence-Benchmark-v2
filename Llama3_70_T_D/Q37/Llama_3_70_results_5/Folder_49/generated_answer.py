def filter_chars(s):
    chars_to_remove = [chr(i) for i in range(42, 98) if '*' <= chr(i) <= 'b']
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s