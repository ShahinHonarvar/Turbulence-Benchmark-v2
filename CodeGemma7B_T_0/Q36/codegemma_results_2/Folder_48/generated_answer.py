def filter_chars(text):
    filtered_text = ''
    for i in range(len(text)):
        if i < 154 or i >= 222 or (text[i] > 'A' and text[i] < 'f'):
            filtered_text += text[i]
    return filtered_text