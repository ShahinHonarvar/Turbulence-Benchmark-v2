def filter_chars(text):
    for i in range(18, 38):
        if text[i] > ')' and text[i] < 'P':
            text = text.replace(text[i], '')
    return text