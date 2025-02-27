def filter_chars(string):
    chars_to_remove = [char for char in string[44:48] if char > '+' and char < 'l']
    for char in chars_to_remove:
        string = string.replace(char, '')
    return string