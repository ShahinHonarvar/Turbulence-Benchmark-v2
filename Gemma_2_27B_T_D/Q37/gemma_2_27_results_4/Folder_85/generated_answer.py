def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if i < 28 or i > 65 or char < 'O' or (char > 'd'):
            result.append(char)
    return ''.join(result)