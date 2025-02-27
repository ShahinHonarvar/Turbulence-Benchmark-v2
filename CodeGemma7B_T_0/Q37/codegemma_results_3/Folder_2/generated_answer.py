def filter_chars(text):
    filtered_text = ''
    for i in range(len(text)):
        if i >= 477 and i <= 984 and (text[i] >= ',') and (text[i] <= 'V'):
            continue
        else:
            filtered_text += text[i]
    return filtered_text