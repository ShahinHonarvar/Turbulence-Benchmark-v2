def filter_chars(text):
    for i in range(422, 853):
        letter = text[i]
        if 'D' < letter < 'J':
            text = text.replace(letter, '')
    return text