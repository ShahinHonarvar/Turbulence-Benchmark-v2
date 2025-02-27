def filter_chars(text):
    result = []
    for i, char in enumerate(text):
        if i < 57 or i > 96 or char < '<' or (char > 'w'):
            result.append(char)
    return ''.join(result)