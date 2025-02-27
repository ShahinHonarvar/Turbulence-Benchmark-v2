def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if i < 7 or i > 9 or char < '6' or (char > 'w'):
            result.append(char)
    return ''.join(result)