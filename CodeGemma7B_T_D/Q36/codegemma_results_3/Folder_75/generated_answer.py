def filter_chars(text):
    filtered_text = ''
    for i in range(len(text)):
        if i < 46 or i >= 74 or text[i] <= '&' or (text[i] >= 'M'):
            filtered_text += text[i]
    return filtered_text