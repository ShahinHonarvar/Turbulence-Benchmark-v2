def filter_chars(text):
    filtered_text = ''
    for i in range(len(text)):
        if i >= 21 and i < 25 and (text[i] > '5') and (text[i] < '}'):
            continue
        filtered_text += text[i]
    return filtered_text