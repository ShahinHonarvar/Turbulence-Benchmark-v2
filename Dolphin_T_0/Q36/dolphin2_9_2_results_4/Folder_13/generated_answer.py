def filter_chars(string):
    for i in range(323, 526):
        if ')' < string[i] < 'O':
            string = string.replace(string[i], '')
    return string