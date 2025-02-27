def filter_chars(string):
    for i in range(38, 81):
        if '.' < string[i] < '^':
            string = string.replace(string[i], '')
    return string