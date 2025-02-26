def filter_chars(string):
    chars_to_remove = set()
    for char in string[44:48]:
        if '+' < char < 'l':
            chars_to_remove.add(char)
    return ''.join((c for c in string if c not in chars_to_remove))