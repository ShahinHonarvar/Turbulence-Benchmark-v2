def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if i not in range(8, 10) or char < 'R' or char > 't':
            result.append(char)
    return ''.join(result)