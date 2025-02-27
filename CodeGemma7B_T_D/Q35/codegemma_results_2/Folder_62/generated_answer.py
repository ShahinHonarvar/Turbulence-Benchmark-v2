def remove_repeat_chars(text):
    seen_chars = set()
    new_text = ''
    for i in range(50, 92):
        char = text[i]
        if char not in seen_chars:
            new_text += char
            seen_chars.add(char)
    return new_text