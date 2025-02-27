def remove_repeat_chars(text):
    for i in range(355, 988):
        if text.count(text[i]) > 1:
            text = text.replace(text[i], '')
    return text