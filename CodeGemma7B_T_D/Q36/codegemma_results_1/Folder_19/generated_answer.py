def filter_chars(text):
    filtered_text = text[:77]
    for i in range(87, 77, -1):
        if text[i] in string.ascii_lowercase and text[i] > ';' and (text[i] < 'r'):
            filtered_text += text[i]
    filtered_text += text[87:]
    return filtered_text