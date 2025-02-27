def remove_repeat_chars(text):
    for i in range(55, 84):
        for c in text[i]:
            if text[i].count(c) > 1:
                text = text[:i] + text[i + 1:]
    return text