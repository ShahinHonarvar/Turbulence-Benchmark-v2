def filter_chars(text):
    result = []
    for i in range(len(text)):
        if not (672 <= i < 709 and text[i] > 'X' and (text[i] < '}')):
            result.append(text[i])
    return ''.join(result)