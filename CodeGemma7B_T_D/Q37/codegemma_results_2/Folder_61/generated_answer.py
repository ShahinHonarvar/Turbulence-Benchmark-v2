def filter_chars(text):
    filtered_text = ''
    for i in range(len(text)):
        if i >= 5 and i <= 6:
            if text[i] >= 'G' and text[i] <= 'p':
                continue
        filtered_text += text[i]
    return filtered_text