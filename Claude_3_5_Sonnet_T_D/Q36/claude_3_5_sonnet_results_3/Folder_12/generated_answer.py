def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if 32 < i < 84:
            if 'm' < char < 'w':
                continue
        result.append(char)
    return ''.join(result)