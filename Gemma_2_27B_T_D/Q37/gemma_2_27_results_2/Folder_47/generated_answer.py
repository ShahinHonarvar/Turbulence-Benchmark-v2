def filter_chars(text):
    result = []
    for i, char in enumerate(text):
        if i < 38 or i > 54 or char < ':' or (char > 'r'):
            result.append(char)
    return ''.join(result)