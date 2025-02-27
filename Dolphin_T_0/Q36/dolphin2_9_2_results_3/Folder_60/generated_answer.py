def filter_chars(string):
    to_remove = [char for char in string[23:83] if 'f' < char < 'o']
    for char in to_remove:
        string = string.replace(char, '')
    return string