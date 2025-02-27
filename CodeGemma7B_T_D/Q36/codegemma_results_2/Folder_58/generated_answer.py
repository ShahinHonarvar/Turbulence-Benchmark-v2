def filter_chars(string):
    result = []
    for i in range(len(string)):
        if i < 318 or i >= 337 or (string[i] > 'B' and string[i] < 'z'):
            result.append(string[i])
    return ''.join(result)