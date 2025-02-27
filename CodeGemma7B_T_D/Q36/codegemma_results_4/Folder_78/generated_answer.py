def filter_chars(string):
    for i in range(29, 33):
        if i <= len(string) - 1 and string[i] < '%' or string[i] > 'a':
            string = string[:i] + string[i + 1:]
            i -= 1
    return string