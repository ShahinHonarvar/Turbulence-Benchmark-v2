def filter_chars(text):
    filtered_text = ''
    for i in range(len(text)):
        if i < 10 or i >= 79 or text[i] <= '?' or (text[i] >= 'm'):
            filtered_text += text[i]
    return filtered_text