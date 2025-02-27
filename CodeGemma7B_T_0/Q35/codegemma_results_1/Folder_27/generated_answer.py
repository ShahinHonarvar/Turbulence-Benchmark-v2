def remove_repeat_chars(text):
    seen = set()
    new_text = []
    for i in range(len(text)):
        if i < 86 or i > 89:
            if text[i] not in seen:
                new_text.append(text[i])
                seen.add(text[i])
    return ''.join(new_text)