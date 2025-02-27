def filter_chars(text):
    for i in range(63, 89):
        char = chr(i)
        if char > '*' and char < 'w':
            text = text.replace(char, '')
    return text