def filter_chars(s):
    indices = list(range(43, 69))
    to_remove = [char for char in s[43:69] if 'B' < char < 'r']
    for char in to_remove:
        s = s.replace(char, '')
    return s