def filter_chars(s):
    chars_to_remove = [char for char in s[309:591] if 'S' < char < 'm']
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s