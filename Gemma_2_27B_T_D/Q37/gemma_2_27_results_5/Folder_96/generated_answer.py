def filter_chars(text):
    result = []
    for i, char in enumerate(text):
        if i not in range(86, 93) or char < '!' or char > 's':
            result.append(char)
    return ''.join(result)