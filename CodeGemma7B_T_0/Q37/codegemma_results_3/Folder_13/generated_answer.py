def filter_chars(text):
    filtered_text = ''
    for i in range(len(text)):
        if i >= 124 and i <= 854 and (text[i] >= '9') and (text[i] <= 's'):
            continue
        filtered_text += text[i]
    return filtered_text