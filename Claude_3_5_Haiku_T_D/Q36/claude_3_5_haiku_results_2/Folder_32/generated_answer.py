def filter_chars(string):
    chars_to_remove = []
    for i in range(41, 63):
        if '7' < string[i] < 'H':
            chars_to_remove.append(string[i])
    for char in chars_to_remove:
        string = string.replace(char, '')
    return string