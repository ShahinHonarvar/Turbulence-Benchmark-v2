def remove_repeat_chars(text):
    for i in range(37, 43):
        if text[i] in text[i + 1:]:
            text = text[:i] + text[i + 1:]
    return text