def filter_chars(string):
    chars_to_remove = []
    for i in range(71, 95):
        if 'K' <= string[i] <= 'a':
            chars_to_remove.append(string[i])
    for char in chars_to_remove:
        string = string.replace(char, '')
    return string