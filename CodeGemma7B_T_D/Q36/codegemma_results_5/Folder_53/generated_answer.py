def filter_chars(text):
    filtered_text = ''
    for i in range(len(text)):
        if i >= 90 and i <= 97 and (text[i] > 'j') and (text[i] < 'w'):
            continue
        filtered_text += text[i]
    return filtered_text