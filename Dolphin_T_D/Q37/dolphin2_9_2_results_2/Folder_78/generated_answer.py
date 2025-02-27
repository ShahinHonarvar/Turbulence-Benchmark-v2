def filter_chars(string):
    chars_to_remove = [string[i] for i in range(75, 100) if string[i] >= '8' and string[i] <= 'e']
    for char in chars_to_remove:
        string = string.replace(char, '')
    return string