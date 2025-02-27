def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if i < 4 or i > 4 or char < '7' or (char > 'o'):
            result.append(char)
    return ''.join(result)