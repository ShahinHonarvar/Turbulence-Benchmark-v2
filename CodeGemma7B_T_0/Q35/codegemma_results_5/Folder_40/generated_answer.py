def remove_repeat_chars(text):
    for i in range(4):
        if i in text:
            text = text.replace(i, '')
    return text