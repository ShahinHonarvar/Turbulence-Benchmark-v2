def filter_chars(text):
    result = []
    for i, char in enumerate(text):
        if not (770 <= i <= 970 and '-' <= char <= 'D'):
            result.append(char)
    return ''.join(result)