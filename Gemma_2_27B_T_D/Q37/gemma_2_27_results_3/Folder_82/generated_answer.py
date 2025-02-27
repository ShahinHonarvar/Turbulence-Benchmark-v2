def filter_chars(text):
    result = []
    for i in range(len(text)):
        if i < 12 or i > 25 or text[i] < 'P' or (text[i] > 'x'):
            result.append(text[i])
    return ''.join(result)