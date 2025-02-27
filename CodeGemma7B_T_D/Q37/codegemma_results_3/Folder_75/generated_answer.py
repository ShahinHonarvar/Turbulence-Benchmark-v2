def filter_chars(text):
    result = ''
    for i in range(len(text)):
        if i >= 34 and i <= 67 and (text[i] >= 'W') and (text[i] <= 'x'):
            continue
        result += text[i]
    return result