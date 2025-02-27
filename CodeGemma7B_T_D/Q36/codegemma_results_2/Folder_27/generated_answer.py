def filter_chars(text):
    new_text = ''
    for i in range(len(text)):
        if text[i] == text[i].lower():
            new_text += text[i]
    return new_text