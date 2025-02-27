def filter_chars(text):
    filtered_text = text[:14]
    for i in range(20, 70):
        if text[i] > '9' and text[i] < 'K':
            continue
        filtered_text += text[i]
    filtered_text += text[70:]
    return filtered_text