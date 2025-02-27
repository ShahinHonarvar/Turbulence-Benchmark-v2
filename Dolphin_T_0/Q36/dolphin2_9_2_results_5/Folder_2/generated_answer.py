def filter_chars(string):
    to_remove = [char for char in string[421:854] if 'D' < char < 'J']
    for remove_char in to_remove:
        string = string.replace(remove_char, '')
    return string