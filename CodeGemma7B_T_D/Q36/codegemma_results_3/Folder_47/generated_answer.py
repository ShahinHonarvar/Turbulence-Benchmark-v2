def filter_chars(text):
    new_text = ''
    for i in range(len(text)):
        if i not in range(45, 57):
            new_text += text[i]
    return new_text