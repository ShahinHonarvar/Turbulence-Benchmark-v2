def filter_chars(text):
    for i in range(299, 418):
        if text[i] > '9' and text[i] < 'P':
            text = text.replace(text[i], '')
    return text