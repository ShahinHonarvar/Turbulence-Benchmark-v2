def remove_repeat_chars(text):
    seen = set()
    new_text = ''
    for i, char in enumerate(text):
        if char in seen:
            continue
        if i < 57 or i >= 85:
            seen.add(char)
            new_text += char
    return new_text