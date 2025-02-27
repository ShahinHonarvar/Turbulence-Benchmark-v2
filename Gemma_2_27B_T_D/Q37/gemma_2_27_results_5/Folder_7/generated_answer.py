def filter_chars(string):
    for i in range(521, 723):
        if i < len(string):
            char = string[i]
            if char >= '>' and char <= '_':
                string = string.replace(char, '')
    return string