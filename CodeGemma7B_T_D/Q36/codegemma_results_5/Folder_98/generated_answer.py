def filter_chars(text):
    filtered_text = ''
    for i in range(len(text)):
        if i < 4 or i >= 8 or text[i] <= '1' or (text[i] >= 'J'):
            filtered_text += text[i]
    return filtered_text