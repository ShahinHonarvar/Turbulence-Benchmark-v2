def filter_chars(text):
    filtered_text = ''
    for i in range(len(text)):
        if i >= 88 and i <= 90 and (text[i] >= 'J') and (text[i] <= 'Q'):
            filtered_text += ''
        else:
            filtered_text += text[i]
    return filtered_text