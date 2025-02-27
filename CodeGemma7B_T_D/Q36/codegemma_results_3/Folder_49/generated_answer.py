def filter_chars(str):
    new_str = list(str)
    for i in range(46, 91):
        if new_str[i] > 'D' and new_str[i] < 'H':
            new_str[i] = None
    return ''.join([i for i in new_str if i != None])