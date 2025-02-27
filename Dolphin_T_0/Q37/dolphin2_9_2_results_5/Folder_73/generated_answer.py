def filter_chars(string):
    chars_to_remove = [char for char in string[22:86] if char >= '7' and char <= 'e']
    for char in chars_to_remove:
        string = string.replace(char, '')
    return string