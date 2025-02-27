def filter_chars(text):
    filtered_text = ''
    for i in range(len(text)):
        if i >= 19 and i <= 90 and (text[i] >= 'F') and (text[i] <= 'h'):
            continue
        filtered_text += text[i]
    return filtered_text