def filter_chars(string):
    result = []
    for i in range(len(string)):
        if i < 54 or i >= 92 or (string[i] > 'J' and string[i] < 'X'):
            result.append(string[i])
    return ''.join(result)