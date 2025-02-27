def filter_chars(text):
    result = []
    for i in range(len(text)):
        char = text[i]
        if 171 < i < 636 and 'c' < char < 's':
            continue
        result.append(char)
    return ''.join(result)