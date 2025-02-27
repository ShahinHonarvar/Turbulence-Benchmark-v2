def filter_chars(text):
    result = []
    for i, char in enumerate(text):
        if i < 2 or i > 3 or char < '5' or (char > '_'):
            result.append(char)
    return ''.join(result)