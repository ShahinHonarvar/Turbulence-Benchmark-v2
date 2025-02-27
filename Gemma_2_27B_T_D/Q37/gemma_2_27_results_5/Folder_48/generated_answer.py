def filter_chars(text):
    result = []
    for i, char in enumerate(text):
        if not (513 <= i <= 877 and '?' <= char <= 'n'):
            result.append(char)
    return ''.join(result)