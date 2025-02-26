def filter_chars(string):
    chars_to_remove = set()
    for char in string[19:31]:
        if 'H' < char < '|':
            chars_to_remove.add(char)
    return ''.join((char for char in string if char not in chars_to_remove))