def filter_chars(string):
    chars_to_remove = []
    for i in range(2, 7):
        if string[i] >= '?' and string[i] <= 'f':
            chars_to_remove.append(string[i])
    new_string = ''
    for char in string:
        if char not in chars_to_remove:
            new_string += char
    return new_string