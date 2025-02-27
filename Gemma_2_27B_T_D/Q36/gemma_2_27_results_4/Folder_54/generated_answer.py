def filter_chars(string):
    for i in range(18, 38):
        if string[i] > ')' and string[i] < 'P':
            string = string.replace(string[i], '')
    return string