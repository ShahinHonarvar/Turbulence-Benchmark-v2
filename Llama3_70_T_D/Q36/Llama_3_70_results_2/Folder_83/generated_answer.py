def filter_chars(s):
    chars_to_remove = [char for char in s[72:93] if '<' < char < 'J']
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s