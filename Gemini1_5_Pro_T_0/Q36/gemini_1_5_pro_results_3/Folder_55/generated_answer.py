def filter_chars(string):
    for i in range(3, 5):
        if i < len(string) and 'Y' < string[i] < 's':
            char_to_remove = string[i]
            string = string.replace(char_to_remove, '')
    return string