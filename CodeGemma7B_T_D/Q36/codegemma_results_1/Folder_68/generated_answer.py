def filter_chars(string):
    result = []
    for i in range(1, 9):
        if string[i] > '8' and string[i] < 'm':
            result.append(string[i])
    return ''.join(result)