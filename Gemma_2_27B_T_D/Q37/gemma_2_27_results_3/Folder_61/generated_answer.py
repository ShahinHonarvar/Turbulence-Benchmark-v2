def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if i < 5 or i > 6 or char < 'G' or (char > 'p'):
            result.append(char)
    return ''.join(result)