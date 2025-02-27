def filter_chars(text):
    for char in text[31:73]:
        if char > 'M' and char < 'j':
            text = text.replace(char, '')
    return text