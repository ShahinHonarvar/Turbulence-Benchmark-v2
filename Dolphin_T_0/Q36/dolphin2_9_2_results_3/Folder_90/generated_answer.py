def filter_chars(string):
    to_remove = []
    for i in range(344, 874):
        if 'f' < string[i] < '~':
            to_remove.append(string[i])
    for char in to_remove:
        string = string.replace(char, '')
    return string