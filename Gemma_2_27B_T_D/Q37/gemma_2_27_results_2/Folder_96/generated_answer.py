def filter_chars(text):
    result = []
    for i, char in enumerate(text):
        if not (86 <= i <= 92 and '!' <= char <= 's'):
            result.append(char)
    return ''.join(result)