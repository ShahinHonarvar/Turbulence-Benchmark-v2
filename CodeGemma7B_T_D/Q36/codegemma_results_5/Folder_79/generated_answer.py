def filter_chars(text):
    filtered_text = ''
    for i in range(len(text)):
        if 11 < i < 46 and text[i] > '!' and (text[i] < 'A'):
            continue
        filtered_text += text[i]
    return filtered_text