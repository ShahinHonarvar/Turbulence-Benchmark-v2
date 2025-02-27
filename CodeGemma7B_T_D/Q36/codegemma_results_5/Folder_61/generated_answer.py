def filter_chars(text):
    result = []
    for i in range(len(text)):
        if i not in range(3, 9):
            result.append(text[i])
    return ''.join(result)