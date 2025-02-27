def filter_chars(text):
    result = []
    for i, char in enumerate(text):
        if i >= 69 and i <= 80 and ('@' <= char <= 'p'):
            continue
        result.append(char)
    return ''.join(result)