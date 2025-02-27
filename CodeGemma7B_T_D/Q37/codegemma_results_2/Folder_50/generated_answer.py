def filter_chars(text):
    new_text = ''
    for i in range(len(text)):
        if i >= 71 and i <= 96 and (text[i] >= '_') and (text[i] <= 'o'):
            continue
        new_text += text[i]
    return new_text