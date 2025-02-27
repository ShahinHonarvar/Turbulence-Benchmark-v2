def filter_chars(string):
    chars_to_remove = []
    for i in range(124, 855):
        char = chr(i)
        if char >= '9' and char <= 's':
            chars_to_remove.append(char)
    for char in chars_to_remove:
        string = string.replace(char, '')
    return string