def filter_chars(string):
    chars_to_remove = []
    for i in range(72, 93):
        char = string[i]
        if char > '<' and char < 'J':
            chars_to_remove.append(char)
    for char in chars_to_remove:
        string = string.replace(char, '')
    return string