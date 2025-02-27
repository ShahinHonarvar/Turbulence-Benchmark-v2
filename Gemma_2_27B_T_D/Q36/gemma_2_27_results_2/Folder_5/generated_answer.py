def filter_chars(text):
    result = []
    for i, char in enumerate(text):
        if 55 <= i < 66 and 'f' < char < '|':
            text = text.replace(char, '')
        result.append(char)
    return ''.join(result)