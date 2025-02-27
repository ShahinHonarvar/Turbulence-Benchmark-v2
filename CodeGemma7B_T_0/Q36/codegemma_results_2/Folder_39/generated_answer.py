def filter_chars(text):
    filtered_text = ''
    for i in range(len(text)):
        if i < 43 or i > 59 or text[i] <= '5' or (text[i] >= 'C'):
            filtered_text += text[i]
    return filtered_text