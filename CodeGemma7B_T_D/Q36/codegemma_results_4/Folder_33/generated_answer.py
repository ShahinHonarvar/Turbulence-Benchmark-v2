def filter_chars(text):
    filtered_text = []
    for i in range(len(text)):
        if i >= 299 and i < 418 and (text[i] > '9') and (text[i] < 'P'):
            continue
        filtered_text.append(text[i])
    return ''.join(filtered_text)