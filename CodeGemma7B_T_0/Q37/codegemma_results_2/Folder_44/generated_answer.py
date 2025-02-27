def filter_chars(text):
    filtered_text = ''
    for i in range(len(text)):
        if i >= 21 and i <= 43 and (text[i] >= '+') and (text[i] <= '8'):
            continue
        else:
            filtered_text += text[i]
    return filtered_text