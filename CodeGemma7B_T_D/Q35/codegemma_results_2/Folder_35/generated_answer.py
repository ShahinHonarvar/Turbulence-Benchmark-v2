def remove_repeat_chars(text):
    for i in range(77, 84):
        count = text.count(text[i])
        while count > 1:
            text = text[:i] + text[i + 1:]
            count -= 1
    return text