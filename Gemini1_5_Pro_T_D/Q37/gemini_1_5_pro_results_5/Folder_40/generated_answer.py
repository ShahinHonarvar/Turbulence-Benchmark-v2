def filter_chars(string):
    for i in range(0, 2):
        if i < len(string) and '*' <= string[i] <= 's':
            char_to_remove = string[i]
            string = string.replace(char_to_remove, '')
    return string