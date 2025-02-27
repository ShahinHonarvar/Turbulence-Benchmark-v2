def remove_repeat_chars(text):
    seen = set()
    new_text = []
    for i, char in enumerate(text):
        if 43 < i < 70 and char in seen:
            continue
        seen.add(char)
        new_text.append(char)
    return ''.join(new_text)