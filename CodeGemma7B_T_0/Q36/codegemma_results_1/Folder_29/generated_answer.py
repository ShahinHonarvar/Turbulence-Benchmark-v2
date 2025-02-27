def filter_chars(text):
    filtered_text = ''
    for i in range(len(text)):
        if i not in range(46, 68):
            filtered_text += text[i]
    return filtered_text