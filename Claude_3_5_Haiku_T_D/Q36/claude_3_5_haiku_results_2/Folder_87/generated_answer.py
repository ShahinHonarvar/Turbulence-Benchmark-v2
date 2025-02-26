def filter_chars(s):
    chars_to_remove = [char for char in s[33:61] if '3' < char < 'D']
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s