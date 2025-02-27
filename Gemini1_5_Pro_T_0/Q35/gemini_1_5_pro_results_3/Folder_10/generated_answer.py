def remove_repeat_chars(text):
    seen_chars = set()
    new_text = ''
    for i, char in enumerate(text):
        if 36 < i < 54:
            if char in seen_chars:
                continue
            elif text[36:54].count(char) > 1:
                seen_chars.add(char)
                continue
            else:
                new_text += char
            continue
        new_text += char
    return new_text