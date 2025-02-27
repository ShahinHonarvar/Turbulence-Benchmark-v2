def filter_chars(text):
    filtered_text = ''
    for i in range(len(text)):
        if i >= 38 and i <= 99 and (text[i] >= 'A') and (text[i] <= 'Q'):
            continue
        else:
            filtered_text += text[i]
    return filtered_text