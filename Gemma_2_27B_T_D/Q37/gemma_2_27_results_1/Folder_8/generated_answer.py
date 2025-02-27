def filter_chars(text):
    result = []
    for i, char in enumerate(text):
        if i < 41 or i > 86 or char < 'S' or (char > 's'):
            result.append(char)
    return ''.join(result)