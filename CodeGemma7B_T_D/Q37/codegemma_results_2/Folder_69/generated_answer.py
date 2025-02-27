def filter_chars(text):
    filtered_text = ''
    for i in range(len(text)):
        if i >= 114 and i <= 639 and (text[i] >= '!') and (text[i] <= 'x'):
            continue
        filtered_text += text[i]
    return filtered_text