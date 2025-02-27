def filter_chars(text):
    filtered_text = ''
    for i in range(len(text)):
        if i >= 138 and i <= 920 and (text[i] >= '6') and (text[i] <= 'A'):
            continue
        filtered_text += text[i]
    return filtered_text