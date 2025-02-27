def filter_chars(text):
    filtered_text = []
    for i in range(len(text)):
        if i < 27 or i >= 75 or (text[i] > 'A' and text[i] < 'i'):
            filtered_text.append(text[i])
    return ''.join(filtered_text)