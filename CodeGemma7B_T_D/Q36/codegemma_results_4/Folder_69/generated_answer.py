def filter_chars(string):
    new_str = ''
    for i in range(343, 665):
        if string[i] > '%' and string[i] < 'U':
            continue
        else:
            new_str += string[i]
    return new_str