def filter_chars(text):
    result = []
    for char in text:
        if ord(char) < 57 or ord(char) > 96 or char < '<' or (char > 'w'):
            result.append(char)
    return ''.join(result)