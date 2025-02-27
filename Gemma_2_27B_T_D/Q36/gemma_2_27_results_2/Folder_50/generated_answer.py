def filter_chars(text):
    for i in range(61, 88):
        char = chr(i)
        if char > '%' and char < 'q':
            text = text.replace(char, '')
    return text