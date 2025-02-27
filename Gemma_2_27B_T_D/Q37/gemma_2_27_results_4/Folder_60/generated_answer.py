def filter_chars(text):
    result = []
    for i, char in enumerate(text):
        if i < 12 or i > 77 or char < ':' or (char > 'L'):
            result.append(char)
    return ''.join(result)