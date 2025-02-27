def filter_chars(text):
    for index in range(32, 84):
        char = text[index]
        if char > 'm' and char < 'w':
            text = text[:index] + text[index + 1:]
            index -= 1
    return text