def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if i < 22 or i > 85 or char < '7' or (char > 'e'):
            result.append(char)
    return ''.join(result)