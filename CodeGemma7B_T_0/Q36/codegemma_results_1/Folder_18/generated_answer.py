def filter_chars(text):
    filtered_text = ''
    for i in range(len(text)):
        if i not in range(587, 648):
            filtered_text += text[i]
    return filtered_text