def filter_chars(text):
    result = []
    for i, char in enumerate(text):
        if i < 13 or i > 28 or char < 'c' or (char > 'n'):
            result.append(char)
    return ''.join(result)