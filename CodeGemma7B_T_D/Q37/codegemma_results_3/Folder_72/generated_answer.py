def filter_chars(text):
    filtered_text = ''
    text_length = len(text)
    text_range = text_length - (text_length - 35)
    for i in range(text_range):
        char = text[i]
        if (i >= 35 and i <= 51) and (char >= 'H' and char <= 's'):
            continue
        filtered_text += char
    return filtered_text