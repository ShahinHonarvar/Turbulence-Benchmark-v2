def filter_chars(text):
    filtered_text = ''
    for i in range(len(text)):
        if i < 42 or i >= 78 or text[i] <= '!' or (text[i] >= '?'):
            filtered_text += text[i]
    return filtered_text