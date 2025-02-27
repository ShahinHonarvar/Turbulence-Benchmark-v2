def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if i < 34 or i > 67 or char < 'W' or (char > 'x'):
            result.append(char)
    return ''.join(result)