def filter_chars(text):
    filtered_text = ''
    for i in range(len(text)):
        if i < 2 or i >= 7 or text[i] < 'h' or (text[i] >= 'k'):
            filtered_text += text[i]
    return filtered_text