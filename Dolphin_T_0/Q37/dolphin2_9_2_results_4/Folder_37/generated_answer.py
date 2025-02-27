def filter_chars(string):
    for i in range(17, 64):
        if string[i] >= 'O' and string[i] <= '^':
            string = string.replace(string[i], '')
    return string