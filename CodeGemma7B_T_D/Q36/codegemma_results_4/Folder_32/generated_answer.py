def filter_chars(string):
    for i in range(40, 63):
        if string[i] > '7' and string[i] < 'H':
            while string[i] in string:
                string = string[:i] + string[i + 1:]
    return string