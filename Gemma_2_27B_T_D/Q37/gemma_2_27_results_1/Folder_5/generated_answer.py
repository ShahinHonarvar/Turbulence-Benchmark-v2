def filter_chars(text):
    result = []
    for i, char in enumerate(text):
        if not (24 <= i <= 82 and '5' <= char <= '<'):
            result.append(char)
    return ''.join(result)