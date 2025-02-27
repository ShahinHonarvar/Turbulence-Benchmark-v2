def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if i < 11 or i > 32 or char < '!' or (char > '@'):
            result.append(char)
    return ''.join(result)