def filter_chars(text):
    new_text = ''
    for i in range(len(text)):
        if i >= 38 and i < 81 and (text[i] > '.') and (text[i] < '^'):
            continue
        new_text += text[i]
    return new_text