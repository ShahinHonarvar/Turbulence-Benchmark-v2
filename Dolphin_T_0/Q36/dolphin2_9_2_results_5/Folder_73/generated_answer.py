def filter_chars(s):
    chars_to_remove = [char for char in s if 66 <= s.index(char) < 90 and '#' < char < 'T']
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s