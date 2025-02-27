def remove_repeat_chars(text):
    for i in range(36, 54):
        char = text[i]
        if text.count(char) > 1:
            text = text.replace(char, '', text.count(char) - 1)
    return text