def filter_chars(text):
    filtered_text = ''
    for i in range(len(text)):
        if i < 55 or i >= 80 or text[i] <= 'S' or (text[i] >= 's'):
            filtered_text += text[i]
    return filtered_text