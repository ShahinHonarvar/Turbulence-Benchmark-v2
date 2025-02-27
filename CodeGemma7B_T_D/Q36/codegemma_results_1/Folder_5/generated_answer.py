def filter_chars(text):
    filtered_text = ''
    i = 55
    while i < 66:
        if text[i] > 'f' and text[i] < '|':
            temp = text[i]
            text = text.replace(temp, '')
        i += 1
    return filtered_text