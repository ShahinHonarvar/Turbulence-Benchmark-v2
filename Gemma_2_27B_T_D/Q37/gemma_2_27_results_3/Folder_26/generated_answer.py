def filter_chars(text):
    result = []
    for i, char in enumerate(text):
        if i < 20 or i > 62 or char < 'i' or (char > 'k'):
            result.append(char)
    return ''.join(result)