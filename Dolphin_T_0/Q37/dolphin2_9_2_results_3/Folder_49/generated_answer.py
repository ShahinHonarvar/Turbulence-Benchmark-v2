def filter_chars(string):
    char_range = string[42:98]
    for char in char_range:
        if char >= '*' and char <= 'b':
            string = string.replace(char, '')
    return string