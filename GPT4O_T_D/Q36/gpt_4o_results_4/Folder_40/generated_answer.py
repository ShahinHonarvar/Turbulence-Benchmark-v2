def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if 1 < i < 7 and '-' < char < 'L':
            continue
        result.append(char)
    return ''.join(result)