def filter_chars(text):
    filtered_text = ''
    for i in range(len(text)):
        if i >= 27 and i <= 85 and (text[i] >= 'c') and (text[i] <= 'i'):
            continue
        filtered_text += text[i]
    return filtered_text