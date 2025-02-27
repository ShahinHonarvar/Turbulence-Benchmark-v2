def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if 603 <= i <= 759 and 'Q' <= char <= 'h':
            continue
        result.append(char)
    return ''.join(result)