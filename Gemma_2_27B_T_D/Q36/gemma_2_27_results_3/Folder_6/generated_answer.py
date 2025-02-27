def filter_chars(string):
    result = []
    for i, char in enumerate(string):
        if 31 <= i < 70 and 'B' < char < 'v':
            string = string.replace(char, '')
        result.append(char)
    return ''.join(result)