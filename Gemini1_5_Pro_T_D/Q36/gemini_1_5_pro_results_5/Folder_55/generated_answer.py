def filter_chars(string):
    chars_to_remove = []
    for i in range(3, 5):
        if i < len(string):
            char = string[i]
            if char > 'Y' and char < 's':
                chars_to_remove.append(char)
    for char in chars_to_remove:
        string = string.replace(char, '')
    return string