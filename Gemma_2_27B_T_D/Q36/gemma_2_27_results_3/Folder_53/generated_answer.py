def filter_chars(text):
    result = []
    for i, char in enumerate(text):
        if 90 <= i < 97 and 'j' < char < 'w':
            text = text.replace(char, '')
        result.append(char)
    return ''.join(result)