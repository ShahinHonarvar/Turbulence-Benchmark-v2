def filter_chars(string):
    result = []
    for i, char in enumerate(string):
        if not (227 <= i <= 235 and 'D' <= char <= 'u'):
            result.append(char)
    return ''.join(result)