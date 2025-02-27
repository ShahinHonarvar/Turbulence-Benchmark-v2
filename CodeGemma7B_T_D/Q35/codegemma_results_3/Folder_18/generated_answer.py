def remove_repeat_chars(text):
    seen_chars = []
    new_text = ''
    for i, char in enumerate(text):
        if 55 < i < 91 and char in seen_chars:
            continue
        seen_chars.append(char)
        new_text += char
    return new_text