def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if i < 11 or i > 72 or char < 'i' or (char > 'v'):
            result.append(char)
    return ''.join(result)