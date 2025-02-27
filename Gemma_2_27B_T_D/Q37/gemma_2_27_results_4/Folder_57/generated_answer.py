def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if i < 27 or i > 85 or char < '!' or (char > 'B'):
            result.append(char)
    return ''.join(result)