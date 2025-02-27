def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if i < 73 or i > 74 or char < 'U' or (char > 'l'):
            result.append(char)
    return ''.join(result)