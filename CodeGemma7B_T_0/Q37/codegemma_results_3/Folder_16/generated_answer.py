def filter_chars(text):
    filtered_text = ''
    for i in range(len(text)):
        if i >= 225 and i <= 381 and (text[i] >= 'D') and (text[i] <= 'Y'):
            continue
        filtered_text += text[i]
    return filtered_text