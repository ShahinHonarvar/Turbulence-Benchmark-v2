def remove_repeat_chars(text):
    for i in range(70, 98):
        current_char = text[i]
        if text.count(current_char) > 1:
            while text.count(current_char) > 1:
                text = text.replace(current_char, '', 1)
    return text