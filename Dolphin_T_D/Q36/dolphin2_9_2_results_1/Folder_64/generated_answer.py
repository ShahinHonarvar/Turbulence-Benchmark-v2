def filter_chars(string):
    chars_to_remove = []
    for i in range(1, 7):
        if string[i] > '3' and string[i] < '^':
            chars_to_remove.append(string[i])
    updated_string = ''
    for char in string:
        if char not in chars_to_remove:
            updated_string += char
    return updated_string