def filter_chars(text):
    result = []
    for i, char in enumerate(text):
        if i < 52 or i > 81 or char < 'A' or (char > 'U'):
            result.append(char)
    return ''.join(result)