def remove_repeat_chars(text):
    for i in range(len(text)):
        if i >= 0 and i <= 9 and (text.count(text[i]) > 1):
            text = text.replace(text[i], '')
    return text