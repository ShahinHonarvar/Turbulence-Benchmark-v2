def filter_chars(text):
    new_text = ''
    for i in range(len(text)):
        if text[i] in string.ascii_uppercase and text[i] >= ':' and (text[i] <= 'L'):
            continue
        else:
            new_text += text[i]
    return new_text