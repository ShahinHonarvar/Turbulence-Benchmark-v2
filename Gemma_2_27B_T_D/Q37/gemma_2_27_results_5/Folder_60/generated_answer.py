def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if i < 12 or i > 77 or char < ':' or (char > 'L'):
            result.append(char)
    return ''.join(result)