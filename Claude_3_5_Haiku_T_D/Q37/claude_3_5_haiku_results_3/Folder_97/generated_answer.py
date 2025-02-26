def filter_chars(text):
    result = list(text)
    for i in range(227, 236):
        if 0 <= i < len(text):
            char = text[i]
            if 'D' <= char <= 'u':
                result = [c for c in result if c != char]
    return ''.join(result)