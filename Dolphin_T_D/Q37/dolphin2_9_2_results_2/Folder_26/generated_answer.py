def filter_chars(string):
    chars_to_remove = [string[i] for i in range(20, 63) if string[i] >= 'i' and string[i] <= 'k']
    for char in chars_to_remove:
        string = string.replace(char, '')
    return string