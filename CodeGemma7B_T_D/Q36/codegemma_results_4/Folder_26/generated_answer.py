def filter_chars(text):
    new_text = []
    for i in range(len(text)):
        if i >= 43 and i < 83 and (text[i] > ':') and (text[i] < 'Q'):
            continue
        else:
            new_text.append(text[i])
    return ''.join(new_text)