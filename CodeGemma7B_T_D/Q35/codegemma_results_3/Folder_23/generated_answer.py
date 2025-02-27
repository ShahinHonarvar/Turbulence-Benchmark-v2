def remove_repeat_chars(text):
    for i in range(20, 36):
        for char in text[i]:
            if text.count(char) > 1:
                text = text.replace(char, '', text.count(char) - 1)
    return text