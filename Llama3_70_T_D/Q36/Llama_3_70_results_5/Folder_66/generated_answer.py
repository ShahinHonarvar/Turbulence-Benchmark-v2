def filter_chars(s):
    chars_to_remove = [char for char in s[39:87] if '!' < char < '}']
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s