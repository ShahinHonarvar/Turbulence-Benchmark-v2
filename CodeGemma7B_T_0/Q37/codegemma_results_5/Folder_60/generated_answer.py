def filter_chars(text):
    filtered_text = ''
    for i in range(len(text)):
        if i >= 12 and i <= 77 and (text[i] >= ':') and (text[i] <= 'L'):
            continue
        filtered_text += text[i]
    return filtered_text