def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if i < 2 or i > 6 or char < '?' or (char > 'f'):
            result.append(char)
    return ''.join(result)