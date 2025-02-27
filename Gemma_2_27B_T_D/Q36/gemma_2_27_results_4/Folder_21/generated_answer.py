def filter_chars(text):
    for i in range(219, 403):
        char = text[i]
        if char > '*' and char < '7':
            text = text.replace(char, '')
    return text