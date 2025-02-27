def filter_chars(s):
    chars_to_remove = [char for char in s[672:709] if 'X' < char < '}']
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s