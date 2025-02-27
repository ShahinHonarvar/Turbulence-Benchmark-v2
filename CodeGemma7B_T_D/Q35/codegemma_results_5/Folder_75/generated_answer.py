def remove_repeat_chars(text):
    seen = set()
    new_text = ''
    for i, char in enumerate(text):
        if i >= 20 and i < 51 and (char in seen):
            continue
        seen.add(char)
        new_text += char
    return new_text