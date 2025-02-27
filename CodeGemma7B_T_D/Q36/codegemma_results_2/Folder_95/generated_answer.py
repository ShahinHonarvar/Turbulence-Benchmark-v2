def filter_chars(text):
    filtered_text = ''
    for i in range(len(text)):
        if i < 56 or i >= 86 or text[i] <= '+' or (text[i] >= 'w'):
            filtered_text += text[i]
    return filtered_text