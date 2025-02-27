def filter_chars(string):
    chars_to_remove = set()
    for char in string[770:971]:
        if 'D' >= char >= '-':
            chars_to_remove.add(char)
    return ''.join((char for char in string if char not in chars_to_remove))