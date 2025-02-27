def filter_chars(text):
    for i in range(86, 93):
        if i < len(text) and text[i] >= '!' and (text[i] <= 's'):
            char = text[i]
            text = text.replace(char, '')
    return text