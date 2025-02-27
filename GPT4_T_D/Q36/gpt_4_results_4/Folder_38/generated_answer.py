def filter_chars(s):
    chars_to_remove = [char for char in s[45:48] if '+' < char < 'l']
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s