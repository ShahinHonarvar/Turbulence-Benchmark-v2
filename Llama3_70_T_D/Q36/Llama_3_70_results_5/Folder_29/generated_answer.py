def filter_chars(s):
    chars_to_remove = [char for char in s[46:68] if 'H' < char < 's']
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s