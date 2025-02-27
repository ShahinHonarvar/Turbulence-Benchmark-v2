def filter_chars(text):
    for i in range(38, 70):
        if i < len(text):
            char = text[i]
            if char >= 'H' and char <= 'e':
                text = text.replace(char, '')
    return text