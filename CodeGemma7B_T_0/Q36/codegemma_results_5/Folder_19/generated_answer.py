def filter_chars(text):
    filtered_text = ''
    for i in range(len(text)):
        if i < 77 or i >= 87 or text[i] <= ';' or (text[i] >= 'r'):
            filtered_text += text[i]
    return filtered_text