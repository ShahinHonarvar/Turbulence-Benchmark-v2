def filter_chars(text):
    for i in range(672, 709):
        if text[i] > 'X' and text[i] < '}':
            text = text.replace(text[i], '')
    return text