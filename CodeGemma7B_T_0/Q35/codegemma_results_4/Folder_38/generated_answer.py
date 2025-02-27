def remove_repeat_chars(text):
    seen = set()
    new_text = []
    for i, char in enumerate(text):
        if i < 36 or i >= 85:
            if char not in seen:
                seen.add(char)
                new_text.append(char)
    return ''.join(new_text)