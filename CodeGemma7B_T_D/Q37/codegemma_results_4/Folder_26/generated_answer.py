def filter_chars(text):
    new_text = ''
    for i in range(len(text)):
        if i >= 20 and i <= 62 and (text[i] >= 'i') and (text[i] <= 'k'):
            continue
        else:
            new_text += text[i]
    return new_text