def filter_chars(string):
    chars_to_remove = [string[i] for i in range(29, 98) if '-' <= string[i] <= 'n']
    for char in chars_to_remove:
        string = string.replace(char, '')
    return string