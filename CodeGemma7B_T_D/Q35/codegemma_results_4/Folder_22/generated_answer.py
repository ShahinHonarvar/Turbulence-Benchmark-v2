def remove_repeat_chars(text):
    seen_chars = set()
    new_text = []
    for i, char in enumerate(text):
        if i >= 50 and i < 200 and (char in seen_chars):
            continue
        seen_chars.add(char)
        new_text.append(char)
    return ''.join(new_text)