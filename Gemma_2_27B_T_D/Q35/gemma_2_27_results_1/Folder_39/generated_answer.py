def remove_repeat_chars(text):
    seen = set()
    for i in range(44, 91):
        if text[i] in seen:
            text = text.replace(text[i], '')
        else:
            seen.add(text[i])
    return text