def filter_chars(text):
    result = []
    for i, char in enumerate(text):
        if i < 54 or i > 62 or (not ')' <= char <= '9'):
            result.append(char)
    return ''.join(result)