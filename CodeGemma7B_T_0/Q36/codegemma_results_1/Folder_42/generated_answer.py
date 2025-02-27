def filter_chars(text):
    filtered_text = ''
    for i in range(len(text)):
        if i < 42 or i > 68:
            filtered_text += text[i]
    for i in range(42, 68):
        if text[i] > 't' and text[i] < 'x':
            filtered_text = filtered_text.replace(text[i], '')
    return filtered_text