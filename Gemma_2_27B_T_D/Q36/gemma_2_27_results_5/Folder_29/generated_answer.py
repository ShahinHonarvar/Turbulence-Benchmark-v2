def filter_chars(text):
    result = []
    for i, char in enumerate(text):
        if i < 46 or i >= 68 or (char <= 'H' or char >= 's'):
            result.append(char)
    return ''.join(result)