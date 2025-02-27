def filter_chars(text):
    filtered_text = ''
    for i in range(len(text)):
        if i < 54 or i >= 92 or (text[i] > 'J' and text[i] < 'X'):
            filtered_text += text[i]
    return filtered_text