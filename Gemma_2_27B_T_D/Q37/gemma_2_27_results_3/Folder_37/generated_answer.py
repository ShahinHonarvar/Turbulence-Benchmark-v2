def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if i < 17 or i > 63 or char < 'O' or (char > '^'):
            result.append(char)
    return ''.join(result)