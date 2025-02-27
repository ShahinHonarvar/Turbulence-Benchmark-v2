def filter_chars(string):
    chars_to_remove = [string[i] for i in range(42, 78) if string[i] > '!' and string[i] < '?']
    for char in chars_to_remove:
        string = string.replace(char, '')
    return string