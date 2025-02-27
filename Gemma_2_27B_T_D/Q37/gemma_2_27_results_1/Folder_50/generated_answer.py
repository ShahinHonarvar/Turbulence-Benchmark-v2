def filter_chars(text):
    result = []
    for i, char in enumerate(text):
        if i < 71 or i > 96 or char < '_' or (char > 'o'):
            result.append(char)
    return ''.join(result)