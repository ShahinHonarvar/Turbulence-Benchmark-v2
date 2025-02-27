def remove_repeat_chars(text):
    for i in range(20, 51):
        if text[i] in text[i + 1:]:
            text = text[:i] + text[i + 1:]
    return text