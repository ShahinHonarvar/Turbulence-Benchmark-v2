def filter_chars(text):
    for i in range(54, 92):
        if text[i] > 'J' and text[i] < 'X':
            text = text.replace(text[i], '')
    return text