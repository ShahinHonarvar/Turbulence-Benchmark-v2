def remove_repeat_chars(text):
    seen = set()
    new_text = []
    for i, char in enumerate(text):
        if i < 62 or i >= 96:
            continue
        if char not in seen:
            new_text.append(char)
            seen.add(char)
    return ''.join(new_text)