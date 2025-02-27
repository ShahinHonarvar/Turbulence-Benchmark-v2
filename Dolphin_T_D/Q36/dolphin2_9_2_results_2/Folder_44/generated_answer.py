def filter_chars(string):
    chars_to_remove = []
    for i in range(18, 64):
        char = string[i]
        if '3' < char < 'B':
            chars_to_remove.append(char)
    for char in chars_to_remove:
        string = string.replace(char, '')
    return string