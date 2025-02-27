def filter_chars(text):
    for i in range(54, 63):
        if i >= len(text):
            break
        char = text[i]
        if char >= ')' and char <= '9':
            text = text.replace(char, '')
    return text