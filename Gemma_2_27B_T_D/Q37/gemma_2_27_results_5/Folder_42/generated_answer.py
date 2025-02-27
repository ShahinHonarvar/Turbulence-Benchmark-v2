def filter_chars(text):
    result = []
    for i, char in enumerate(text):
        if i < 73 or i > 74 or char < 'U' or (char > 'l'):
            result.append(char)
    return ''.join(result)