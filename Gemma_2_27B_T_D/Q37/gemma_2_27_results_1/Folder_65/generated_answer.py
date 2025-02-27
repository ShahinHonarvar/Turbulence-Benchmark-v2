def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if i < 61 or i > 70 or char < '0' or (char > '@'):
            result.append(char)
    return ''.join(result)