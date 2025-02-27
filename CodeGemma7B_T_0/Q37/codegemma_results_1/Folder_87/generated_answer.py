def filter_chars(text):
    filtered_text = ''
    for i in range(len(text)):
        if i >= 18 and i <= 81 and (text[i] >= 'W') and (text[i] <= '['):
            continue
        filtered_text += text[i]
    return filtered_text