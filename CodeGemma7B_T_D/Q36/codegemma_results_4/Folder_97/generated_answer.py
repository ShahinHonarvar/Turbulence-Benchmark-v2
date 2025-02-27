def filter_chars(string):
    indices = range(309, 591)
    new_string = []
    for i, char in enumerate(string):
        if i not in indices or (char > 'S' and char < 'm'):
            new_string.append(char)
    return ''.join(new_string)