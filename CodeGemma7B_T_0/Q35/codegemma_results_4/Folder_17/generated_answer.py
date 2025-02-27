def remove_repeat_chars(text):
    seen = set()
    new_text = []
    for i, char in enumerate(text):
        if i < 73 or i >= 84 or char in seen:
            continue
        seen.add(char)
        new_text.append(char)
    return ''.join(new_text)