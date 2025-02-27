def filter_chars(text):
    result = []
    for i, char in enumerate(text):
        if i >= 54 and i <= 62 and (char >= ')') and (char <= '9'):
            continue
        result.append(char)
    return ''.join(result)