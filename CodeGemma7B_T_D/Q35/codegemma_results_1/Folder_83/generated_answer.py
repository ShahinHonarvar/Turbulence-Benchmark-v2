def remove_repeat_chars(text):
    for i in range(100, 200):
        if text[i] in text[i + 1:]:
            while text[i] in text:
                text = text.replace(text[i], '')
    return text