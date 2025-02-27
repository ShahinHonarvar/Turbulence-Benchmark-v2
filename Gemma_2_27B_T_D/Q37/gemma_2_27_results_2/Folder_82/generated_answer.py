def filter_chars(string):
    result = []
    for i, char in enumerate(string):
        if i < 12 or i > 25 or char < 'P' or (char > 'x'):
            result.append(char)
    return ''.join(result)