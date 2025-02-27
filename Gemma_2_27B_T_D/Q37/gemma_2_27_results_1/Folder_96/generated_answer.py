def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if i < 86 or i > 92 or char < '!' or (char > 's'):
            result.append(char)
    return ''.join(result)