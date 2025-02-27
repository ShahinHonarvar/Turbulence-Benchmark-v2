def filter_chars(text):
    result = []
    for i, char in enumerate(text):
        if not (603 <= i <= 759 and 'Q' <= char <= 'h'):
            result.append(char)
    return ''.join(result)