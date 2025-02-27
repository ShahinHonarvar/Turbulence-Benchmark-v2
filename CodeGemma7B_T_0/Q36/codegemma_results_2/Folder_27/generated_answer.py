def filter_chars(text):
    filtered_text = ''
    for i in range(len(text)):
        if i < 48 or i > 75 or (text[i] > '6' and text[i] < '_'):
            filtered_text += text[i]
    return filtered_text