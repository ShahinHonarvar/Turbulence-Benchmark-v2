def filter_chars(s):
    chars_to_filter = [char for char in s[23:83] if 'f' < char < 'o']
    for char in chars_to_filter:
        s = s.replace(char, '')
    return s