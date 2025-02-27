def filter_chars(text):
    filtered_text = ''
    for i in range(len(text)):
        if i < 43 or i >= 83:
            continue
        if text[i] > ':' and text[i] < 'Q':
            filtered_text += text[i]
    return filtered_text