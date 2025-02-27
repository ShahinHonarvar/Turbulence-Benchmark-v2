def filter_chars(text):
    result = []
    for i, char in enumerate(text):
        if i < 35 or i > 51 or char < 'H' or (char > 's'):
            result.append(char)
    return ''.join(result)