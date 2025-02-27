def filter_chars(text):
    filtered_text = ''
    for i in range(len(text)):
        if not (18 <= i < 95 and text[i] > 'K' and (text[i] < 'a')):
            filtered_text += text[i]
    return filtered_text