def filter_chars(text):
    filtered_text = ''
    for i in range(len(text)):
        if 11 <= i <= 72 and text[i] >= 'i' and (text[i] <= 'v'):
            continue
        filtered_text += text[i]
    return filtered_text