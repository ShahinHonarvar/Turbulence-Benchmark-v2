def filter_chars(string):
    chars_to_remove = [char for char in string[587:648] if char > ',' and char < 'c']
    for char in set(chars_to_remove):
        string = string.replace(char, '')
    return string