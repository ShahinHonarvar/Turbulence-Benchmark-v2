def remove_repeat_chars(text):
    for start in range(77, 84):
        if text[start] in text[start + 1:]:
            while text[start] in text:
                text = text.replace(text[start], '', 1)
    return text