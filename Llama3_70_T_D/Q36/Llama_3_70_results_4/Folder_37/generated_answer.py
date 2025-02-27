def filter_chars(s):
    chars_to_remove = [char for char in s[44:59] if '/' < char < '6']
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s