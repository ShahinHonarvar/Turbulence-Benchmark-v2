def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if i < 29 or i > 97 or char < '-' or (char > 'n'):
            result.append(char)
    return ''.join(result)