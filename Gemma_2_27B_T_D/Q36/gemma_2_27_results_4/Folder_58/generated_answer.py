def filter_chars(text):
    result = []
    for i, char in enumerate(text):
        if 318 <= i < 337 and 'B' < char < 'z':
            text = text.replace(char, '')
        result.append(char)
    return ''.join(result)