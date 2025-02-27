def remove_repeat_chars(text):
    new_text = ''
    seen_chars = set()
    for i, char in enumerate(text):
        if i >= 2 and i <= 5 and (char not in seen_chars):
            new_text += char
            seen_chars.add(char)
    return new_text