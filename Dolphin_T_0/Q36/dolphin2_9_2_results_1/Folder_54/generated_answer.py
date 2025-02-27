def filter_chars(string):
    chars_to_remove = [char for char in string[18:38] if ')' < char < 'P']
    for char in chars_to_remove:
        string = string.replace(char, '')
    return string