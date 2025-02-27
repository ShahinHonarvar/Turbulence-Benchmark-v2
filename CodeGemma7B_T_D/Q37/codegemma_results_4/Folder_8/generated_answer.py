def filter_chars(text):
    filtered_text = ''
    for i in range(len(text)):
        if i >= 41 and i <= 86 and (text[i] >= 'S') and (text[i] <= 's'):
            continue
        filtered_text += text[i]
    return filtered_text