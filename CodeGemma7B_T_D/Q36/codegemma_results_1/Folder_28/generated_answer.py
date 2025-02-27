def filter_chars(text):
    for i in range(31, 73):
        while text[i] > 'M' and text[i] < 'j':
            text = text.replace(text[i], '')
    return text