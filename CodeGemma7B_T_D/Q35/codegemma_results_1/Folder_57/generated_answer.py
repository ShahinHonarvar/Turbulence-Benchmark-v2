def remove_repeat_chars(text):
    for i in range(25, 80):
        current_char = text[i]
        if text.count(current_char) > 1:
            text = text.replace(current_char, '', text.count(current_char) - 1)
    return text