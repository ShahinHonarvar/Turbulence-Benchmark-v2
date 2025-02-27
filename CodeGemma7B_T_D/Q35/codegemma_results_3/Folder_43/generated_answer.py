def remove_repeat_chars(text):
    for i in range(len(text)):
        if i >= 10 and i < 28 and (text.count(text[i]) > 1):
            text = text.replace(text[i], '')
    return text