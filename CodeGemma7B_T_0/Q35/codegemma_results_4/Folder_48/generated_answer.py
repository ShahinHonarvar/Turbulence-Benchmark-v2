def remove_repeat_chars(text):
    for i in range(409, 502):
        if text[i] in text[i + 1:]:
            text = text[:i] + text[i + 1:]
    return text