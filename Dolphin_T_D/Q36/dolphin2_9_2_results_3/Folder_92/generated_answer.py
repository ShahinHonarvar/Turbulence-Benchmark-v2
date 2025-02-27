def filter_chars(string):
    chars_to_remove = [string[i] for i in range(1, 6) if string[i] > ',' and string[i] < 'f']
    for char in chars_to_remove:
        string = string.replace(char, '')
    return string