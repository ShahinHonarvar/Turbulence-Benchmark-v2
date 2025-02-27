def filter_chars(text):
    filtered_text = ''
    for i in range(len(text)):
        if i >= 35 and i <= 89 and (text[i] >= 'E') and (text[i] <= 't'):
            continue
        filtered_text += text[i]
    return filtered_text