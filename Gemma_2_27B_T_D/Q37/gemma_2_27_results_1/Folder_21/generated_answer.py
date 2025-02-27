def filter_chars(text):
    result = []
    for i, char in enumerate(text):
        if 603 <= i <= 759 and 'Q' <= char <= 'h':
            continue
        result.append(char)
    return ''.join(result)