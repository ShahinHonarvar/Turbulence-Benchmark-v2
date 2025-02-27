def filter_chars(string):
    result = []
    for i, char in enumerate(string):
        if 36 <= i <= 79 and 'a' <= char <= 'i':
            string = string.replace(char, '')
        result.append(char)
    return ''.join(result)