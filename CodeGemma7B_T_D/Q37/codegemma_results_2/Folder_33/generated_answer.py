def filter_chars(text):
    filtered_text = ''
    for i, c in enumerate(text):
        if i >= 722 and i <= 832 and (c >= 'K') and (c <= 'm'):
            continue
        filtered_text += c
    return filtered_text