def filter_chars(string):
    chars_to_remove = [char for char in string[18:64] if '3' < char < 'B']
    for char in chars_to_remove:
        string = string.replace(char, '')
    return string