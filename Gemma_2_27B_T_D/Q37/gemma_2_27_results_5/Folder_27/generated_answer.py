def filter_chars(text):
    result = []
    for i, char in enumerate(text):
        if i < 43 or i > 80 or char < '=' or (char > 'E'):
            result.append(char)
    return ''.join(result)