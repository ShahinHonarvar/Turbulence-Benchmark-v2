def filter_chars(string):
    chars_to_remove = []
    for i in range(24, 45):
        if i < len(string) and '3' < string[i] < 'I':
            chars_to_remove.append(string[i])
    for char in chars_to_remove:
        string = string.replace(char, '')
    return string