def filter_chars(string):
    for i in range(17, 64):
        if string[i] >= 'O' and string[i] <= '^':
            string = string[:i] + string[i + 1:]
    return string