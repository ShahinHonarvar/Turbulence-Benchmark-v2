def filter_chars(string):
    chars_to_remove = [char for char in string[43:83] if ':' < char < 'Q']
    for char in chars_to_remove:
        string = string.replace(char, '')
    return string