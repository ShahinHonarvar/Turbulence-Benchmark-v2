def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if i < 29 or i > 79 or char < 'K' or (char > 'z'):
            result.append(char)
    return ''.join(result)