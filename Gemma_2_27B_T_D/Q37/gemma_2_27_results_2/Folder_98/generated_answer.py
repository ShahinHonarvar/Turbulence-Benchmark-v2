def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if i < 8 or i > 9 or char < 'R' or (char > 't'):
            result.append(char)
    return ''.join(result)