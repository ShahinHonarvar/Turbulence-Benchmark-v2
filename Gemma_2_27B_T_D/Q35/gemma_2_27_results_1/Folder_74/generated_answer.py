def remove_repeat_chars(text):
    for i in range(69, 97):
        char = text[i]
        if text.count(char, 69, 97) > 1:
            text = text.replace(char, '')
    return text