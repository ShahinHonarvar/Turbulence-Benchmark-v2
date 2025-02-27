def remove_repeat_chars(text):
    for i in range(69, 97):
        for c in text[i]:
            if text.count(c, i, i + 1) > 1:
                text = text.replace(c, '', text.count(c, i, i + 1) - 1)
    return text