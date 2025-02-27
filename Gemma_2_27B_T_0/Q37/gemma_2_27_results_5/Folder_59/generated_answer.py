def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if i < 2 or i > 3 or char < '5' or (char > '_'):
            result.append(char)
    return ''.join(result)