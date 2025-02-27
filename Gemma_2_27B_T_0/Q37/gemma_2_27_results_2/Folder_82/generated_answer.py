def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if i < 12 or i > 25 or char < 'P' or (char > 'x'):
            result.append(char)
    return ''.join(result)