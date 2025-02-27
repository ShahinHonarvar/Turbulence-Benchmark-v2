def filter_chars(s):
    chars_to_remove = [char for char in s[29:33] if '%' < char < 'a']
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s