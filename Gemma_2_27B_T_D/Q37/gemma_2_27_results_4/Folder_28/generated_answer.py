def filter_chars(text):
    result = []
    for i, char in enumerate(text):
        if 20 <= i <= 79 and '!' <= char <= 'T':
            text = text.replace(char, '', text.count(char))
        result.append(char)
    return ''.join(result)