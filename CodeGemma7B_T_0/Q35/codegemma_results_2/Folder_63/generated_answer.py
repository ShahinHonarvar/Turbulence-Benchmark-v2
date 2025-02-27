def remove_repeat_chars(text):
    seen = set()
    new_text = []
    for i, char in enumerate(text):
        if i not in range(81, 86):
            if char not in seen:
                seen.add(char)
                new_text.append(char)
    return ''.join(new_text)