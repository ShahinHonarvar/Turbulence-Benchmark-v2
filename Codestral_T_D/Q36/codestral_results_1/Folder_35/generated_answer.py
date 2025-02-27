def filter_chars(text):
    for char in text[163:658]:
        if '(' < char < ']':
            text = text.replace(char, '')
    return text