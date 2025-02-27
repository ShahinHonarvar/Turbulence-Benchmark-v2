def filter_chars(text):
    for i in range(1, 7):
        char = text[i]
        if '3' < char < '^':
            text = text.replace(char, '')
    return text