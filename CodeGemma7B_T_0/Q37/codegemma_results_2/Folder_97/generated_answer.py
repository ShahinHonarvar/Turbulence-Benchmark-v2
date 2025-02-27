def filter_chars(text):
    filtered_text = ''
    for i in range(len(text)):
        if i >= 227 and i <= 235 and (text[i] >= 'D') and (text[i] <= 'u'):
            continue
        filtered_text += text[i]
    return filtered_text