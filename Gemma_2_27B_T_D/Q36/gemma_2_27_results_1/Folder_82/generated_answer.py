def filter_chars(text):
    result = []
    for i, char in enumerate(text):
        if 69 <= i < 97 and 'V' < char < 'j':
            text = text.replace(char, '')
        result.append(char)
    return ''.join(result)