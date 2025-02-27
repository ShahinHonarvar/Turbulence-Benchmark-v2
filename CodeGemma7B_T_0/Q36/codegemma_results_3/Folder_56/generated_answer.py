def filter_chars(text):
    filtered_text = ''
    for i in range(len(text)):
        if i < 31 or i >= 50 or text[i] <= '/' or (text[i] >= 'J'):
            filtered_text += text[i]
    return filtered_text