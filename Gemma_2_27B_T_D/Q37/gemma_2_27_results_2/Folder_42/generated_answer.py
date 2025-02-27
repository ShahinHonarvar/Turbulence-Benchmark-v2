def filter_chars(text):
    result = []
    for i, char in enumerate(text):
        if i not in range(73, 75) or char < 'U' or char > 'l':
            result.append(char)
    return ''.join(result)