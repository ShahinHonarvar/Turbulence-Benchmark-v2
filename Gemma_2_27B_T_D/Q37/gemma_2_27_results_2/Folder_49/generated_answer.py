def filter_chars(text):
    result = []
    for i in range(len(text)):
        if i < 42 or i > 97:
            result.append(text[i])
        elif text[i] < '*' or text[i] > 'b':
            result.append(text[i])
    return ''.join(result)