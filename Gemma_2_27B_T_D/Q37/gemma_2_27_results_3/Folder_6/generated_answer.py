def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if i < 13 or i > 28 or char < 'c' or (char > 'n'):
            result.append(char)
    return ''.join(result)