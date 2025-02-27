def filter_chars(text):
    result = []
    for i, char in enumerate(text):
        if i < 36 or i > 79 or char < '2' or (char > 's'):
            result.append(char)
    return ''.join(result)