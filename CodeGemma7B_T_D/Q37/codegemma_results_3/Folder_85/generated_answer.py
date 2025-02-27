def filter_chars(text):
    filtered_text = ''
    for i in range(len(text)):
        if i >= 28 and i <= 65 and (text[i] >= 'O') and (text[i] <= 'd'):
            continue
        filtered_text += text[i]
    return filtered_text