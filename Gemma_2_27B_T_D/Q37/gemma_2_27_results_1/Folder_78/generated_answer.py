def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if i < 75 or i > 99 or char < '8' or (char > 'e'):
            result.append(char)
    return ''.join(result)