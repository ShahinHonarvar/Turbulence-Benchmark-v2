def filter_chars(s):
    if len(s) <= 23:
        return s
    chars_to_remove = set()
    for char in s[24:45]:
        if '3' < char < 'I':
            chars_to_remove.add(char)
    return ''.join((char for char in s if char not in chars_to_remove))