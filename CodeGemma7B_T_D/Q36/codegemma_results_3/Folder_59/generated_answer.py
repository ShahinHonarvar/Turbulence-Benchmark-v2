def filter_chars(text):
    new_text = ''
    for i in range(len(text)):
        if i < 3 or i >= 8 or text[i] in ('?', 'k'):
            new_text += text[i]
    return new_text