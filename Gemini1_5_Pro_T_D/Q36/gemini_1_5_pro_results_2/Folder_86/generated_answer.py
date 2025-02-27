def filter_chars(string):
    chars_to_remove = []
    for i in range(672, 709):
        if i >= len(string):
            break
        char = string[i]
        if char > 'X' and char < '}':
            chars_to_remove.append(char)
    for char in chars_to_remove:
        string = string.replace(char, '')
    return string