def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if not (83 <= i <= 99 and '*' <= char <= 'j'):
            result.append(char)
    return ''.join(result)