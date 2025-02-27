def filter_chars(text):
    new_text = ''
    for i in range(len(text)):
        if not (text[i] > '<' and text[i] < '>'):
            new_text += text[i]
    return new_text