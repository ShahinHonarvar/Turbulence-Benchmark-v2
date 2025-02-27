def filter_chars(text):
    for i in range(672, 709):
        char = text[i]
        if char > 'X' and char < '}':
            text = text.replace(char, '')
    return text