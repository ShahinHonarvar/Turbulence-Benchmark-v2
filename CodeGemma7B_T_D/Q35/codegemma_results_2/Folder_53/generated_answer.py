def remove_repeat_chars(text):
    for i in range(200, 202):
        if text[i] in text[i + 1:]:
            text = text.replace(text[i], '', text.count(text[i]))
    return text