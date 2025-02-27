def remove_repeat_chars(text):
    seen = set()
    repeat_chars = set()
    for i, char in enumerate(text):
        if 70 < i < 98:
            if char in seen:
                repeat_chars.add(char)
            else:
                seen.add(char)
    for char in repeat_chars:
        text = text.replace(char, '')
    return text