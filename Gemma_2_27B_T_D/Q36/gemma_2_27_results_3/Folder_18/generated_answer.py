def filter_chars(text):
    for i in range(587, 648):
        char = text[i]
        if ',' < char < 'c':
            text = text.replace(char, '')
    return text