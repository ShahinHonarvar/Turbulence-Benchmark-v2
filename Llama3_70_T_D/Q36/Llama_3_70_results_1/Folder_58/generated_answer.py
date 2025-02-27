def filter_chars(s):
    chars_to_remove = [char for char in s[318:337] if 'B' < char < 'z']
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s