def filter_chars(text):
    for i in range(323, 526):
        char = text[i]
        if char > ')' and char < 'O':
            text = text.replace(char, '')
    return text