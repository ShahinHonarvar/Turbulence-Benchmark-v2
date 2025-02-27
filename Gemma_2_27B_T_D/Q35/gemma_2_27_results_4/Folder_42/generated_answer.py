def remove_repeat_chars(text):
    seen = set()
    for i in range(18, 60):
        if text[i] in seen:
            text = text.replace(text[i], '')
        else:
            seen.add(text[i])
    return text