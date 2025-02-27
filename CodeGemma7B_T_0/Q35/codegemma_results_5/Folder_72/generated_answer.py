def remove_repeat_chars(text):
    seen = set()
    new_text = []
    for i in range(13, 70):
        if text[i] not in seen:
            seen.add(text[i])
            new_text.append(text[i])
    return ''.join(new_text)