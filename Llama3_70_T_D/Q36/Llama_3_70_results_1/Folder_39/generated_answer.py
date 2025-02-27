def filter_chars(s):
    chars_to_remove = [char for char in s[43:59] if '5' < char < 'C']
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s