def filter_chars(text):
    filtered_text = ''
    for i in range(len(text)):
        if i >= 11 and i <= 32 and (text[i] >= '!') and (text[i] <= '@'):
            continue
        filtered_text += text[i]
    return filtered_text