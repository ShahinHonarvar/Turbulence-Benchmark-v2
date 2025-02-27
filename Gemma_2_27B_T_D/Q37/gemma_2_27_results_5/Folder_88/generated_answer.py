def filter_chars(text):
    result = []
    for i, char in enumerate(text):
        if i < 69 or i > 80 or char < '@' or (char > 'p'):
            result.append(char)
    return ''.join(result)