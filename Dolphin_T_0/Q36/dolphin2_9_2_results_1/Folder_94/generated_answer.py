def filter_chars(string):
    chars_to_remove = []
    for i in range(15, 85):
        if 'I' < string[i] < 'M':
            chars_to_remove.append(string[i])
    for char in chars_to_remove:
        string = string.replace(char, '')
    return string