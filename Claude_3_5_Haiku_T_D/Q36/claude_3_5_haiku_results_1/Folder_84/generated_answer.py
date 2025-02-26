def filter_chars(string):
    result = list(string)
    for i in range(172, 636):
        char = result[i]
        if 'c' < char < 's':
            result = [x for x in result if x != char]
    return ''.join(result)