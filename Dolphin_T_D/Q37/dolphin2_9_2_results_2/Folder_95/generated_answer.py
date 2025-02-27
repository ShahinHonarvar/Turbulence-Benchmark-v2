def filter_chars(string):
    to_remove = []
    for index in range(35, 41):
        if ')' <= string[index] <= 'l':
            to_remove.append(string[index])
    for char in to_remove:
        string = string.replace(char, '')
    return string