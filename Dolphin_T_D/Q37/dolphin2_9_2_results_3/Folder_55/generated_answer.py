def filter_chars(string):
    toBeDeleted = [char for char in string[1:6] if char >= '$' and char <= ';']
    for char in toBeDeleted:
        string = string.replace(char, '')
    return string