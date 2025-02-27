def filter_chars(text):
    filtered_text = ''
    for i in range(len(text)):
        if i > 342 and i < 665 and (text[i] > '%') and (text[i] < 'U'):
            continue
        else:
            filtered_text += text[i]
    return filtered_text