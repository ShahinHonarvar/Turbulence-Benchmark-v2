def remove_repeat_chars(text):
    for i in range(450, 905):
        letter = text[i]
        if text.count(letter) > 1:
            text = text.replace(letter, '')
    return text