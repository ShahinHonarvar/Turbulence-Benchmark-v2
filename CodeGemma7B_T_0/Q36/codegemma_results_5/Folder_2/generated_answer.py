def filter_chars(text):
    filtered_text = ''
    for i in range(len(text)):
        if i < 421 or i >= 854 or (text[i] > 'D' and text[i] < 'J'):
            filtered_text += text[i]
    return filtered_text