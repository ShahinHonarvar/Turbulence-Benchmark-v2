def filter_chars(string):
    to_remove = [char for char in string[513:878] if char >= '?' and char <= 'n']
    for char in to_remove:
        string = string.replace(char, '')
    return string