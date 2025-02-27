def insert_after_character(text):
    i = text.find('a')
    while i != -1:
        text = text[:i + 1] + 'a' + text[i + 1:]
        i = text.find('a', i + 2)
    return text