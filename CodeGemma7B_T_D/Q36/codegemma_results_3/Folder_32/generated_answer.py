def filter_chars(text):
    filtered_text = ''
    for i in range(len(text)):
        if i >= 40 and i <= 63 and (text[i] > '7') and (text[i] < 'H'):
            continue
        filtered_text += text[i]
    return filtered_text