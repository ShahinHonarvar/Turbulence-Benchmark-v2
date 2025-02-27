def filter_chars(text):
    filtered_text = ''
    for i in range(len(text)):
        if text[i] >= 'S' and text[i] <= 's' and (i >= 41) and (i <= 86):
            continue
        filtered_text += text[i]
    return filtered_text