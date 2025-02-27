def filter_chars(text):
    filtered_text = ''
    for i in range(len(text)):
        if i < 40 or i > 63 or (text[i] > '7' and text[i] < 'H'):
            filtered_text += text[i]
    return filtered_text