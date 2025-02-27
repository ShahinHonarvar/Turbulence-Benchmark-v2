def filter_chars(text):
    filtered_text = ''
    for i in range(len(text)):
        if i >= 42 and i <= 67 and (text[i] > '6') and (text[i] < 'g'):
            continue
        else:
            filtered_text += text[i]
    return filtered_text