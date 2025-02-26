def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if 477 <= i <= 984 and ',' <= char <= 'V':
            continue
        result.append(char)
    return ''.join(result)