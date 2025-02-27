def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if i < 83 or i > 99 or char < '*' or (char > 'j'):
            result.append(char)
    return ''.join(result)