def filter_chars(s):
    chars_to_filter = [char for char in s[46:57] if 'F' < char < 'n']
    for char in chars_to_filter:
        s = s.replace(char, '')
    return s