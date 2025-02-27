def filter_chars(string):
    result = []
    for i in range(len(string)):
        if i >= 587 and i <= 648 and (string[i] > ',') and (string[i] < 'c'):
            continue
        result.append(string[i])
    return ''.join(result)