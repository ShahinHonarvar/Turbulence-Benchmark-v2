def filter_chars(text):
    for i in range(33, 36):
        char = text[i]
        if char > '>' and char < 'A':
            text = text.replace(char, '')
    return text