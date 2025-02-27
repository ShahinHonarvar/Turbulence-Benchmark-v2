def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if not (513 <= i <= 877 and '?' <= char <= 'n'):
            result.append(char)
    return ''.join(result)