def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if not (770 <= i <= 970 and '-' <= char <= 'D'):
            result.append(char)
    return ''.join(result)