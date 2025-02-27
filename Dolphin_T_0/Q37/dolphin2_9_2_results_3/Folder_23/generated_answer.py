def filter_chars(string):
    for i in range(51, 78):
        if string[i] >= 'V' and string[i] <= 'Y':
            string = string[:i] + string[i + 1:]
    return string