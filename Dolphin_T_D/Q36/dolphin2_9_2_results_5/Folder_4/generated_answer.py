def filter_chars(string):
    chars_to_remove = [char for char in string[42:67] if '6' < char < 'g']
    for char in chars_to_remove:
        string = string.replace(char, '')
    return string