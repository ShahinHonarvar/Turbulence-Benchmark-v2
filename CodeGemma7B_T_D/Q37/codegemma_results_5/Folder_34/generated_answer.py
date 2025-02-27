def filter_chars(text):
    filtered = ''
    for i in range(len(text)):
        if i >= 54 and i <= 62 and (text[i] >= ')') and (text[i] <= '9'):
            continue
        filtered += text[i]
    return filtered