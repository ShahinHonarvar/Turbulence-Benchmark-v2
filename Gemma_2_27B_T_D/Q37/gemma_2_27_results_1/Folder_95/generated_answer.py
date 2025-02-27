def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if i < 35 or i > 40 or char < ')' or (char > 'l'):
            result.append(char)
    return ''.join(result)