def filter_chars(string):
    result = ''
    char_indices = []
    for i in range(len(string)):
        if i > 44 and i < 48:
            char_indices.append(i)
    for i in range(len(char_indices)):
        if string[char_indices[i]] > '+' and string[char_indices[i]] < 'l':
            string = string.replace(string[char_indices[i]], '')
    return string