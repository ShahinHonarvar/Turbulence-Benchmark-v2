def filter_chars(text):
    filtered_text = ''
    for i in range(len(text)):
        if i >= 348 and i <= 852 and (text[i] >= 'J') and (text[i] <= 'b'):
            continue
        filtered_text += text[i]
    return filtered_text