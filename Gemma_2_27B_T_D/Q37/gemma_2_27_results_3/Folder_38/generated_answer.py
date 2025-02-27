def filter_chars(text):
    filtered_text = ''
    for i in range(len(text)):
        if i >= 24 and i <= 79 and (text[i] >= 'a') and (text[i] <= 'f'):
            text = text.replace(text[i], '')
        filtered_text += text[i]
    return filtered_text