def filter_chars(text):
    result = []
    for i, char in enumerate(text):
        if i < 27 or i > 29 or char < ';' or (char > 'b'):
            result.append(char)
    return ''.join(result)