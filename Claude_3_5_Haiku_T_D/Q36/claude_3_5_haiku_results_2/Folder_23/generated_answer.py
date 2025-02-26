def filter_chars(string):
    if len(string) <= 26:
        return string
    chars_to_remove = []
    for i in range(22, 25):
        if '5' < string[i] < '}':
            chars_to_remove.append(string[i])
    for char in chars_to_remove:
        string = string.replace(char, '')
    return string