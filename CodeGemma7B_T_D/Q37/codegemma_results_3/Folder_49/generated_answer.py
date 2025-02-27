def filter_chars(string):
    for i in range(len(string)):
        if 42 <= i <= 97 and '*' <= string[i] <= 'b':
            string = string.replace(string[i], '', 1)
    return string