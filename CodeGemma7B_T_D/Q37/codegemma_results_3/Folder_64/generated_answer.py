def filter_chars(text):
    new_text = ''
    for i in range(len(text)):
        if i < 8 and text[i] >= 'L' and (text[i] <= 'a'):
            continue
        else:
            new_text += text[i]
    return new_text