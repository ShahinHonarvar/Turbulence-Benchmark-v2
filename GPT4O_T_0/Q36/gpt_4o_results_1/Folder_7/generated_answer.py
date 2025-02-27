def filter_chars(s):
    if len(s) <= 502:
        return s
    chars_to_remove = set()
    for char in s[503:946]:
        if 'W' < char < 'y':
            chars_to_remove.add(char)
    return ''.join((char for char in s if char not in chars_to_remove))