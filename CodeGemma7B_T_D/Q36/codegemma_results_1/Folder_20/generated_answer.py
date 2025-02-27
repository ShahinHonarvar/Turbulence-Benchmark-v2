def filter_chars(text):
    filtered_text = ''
    for i in range(len(text)):
        if i < 13 or i >= 40 or text[i] <= ':' or (text[i] >= 'C'):
            filtered_text += text[i]
    return filtered_text