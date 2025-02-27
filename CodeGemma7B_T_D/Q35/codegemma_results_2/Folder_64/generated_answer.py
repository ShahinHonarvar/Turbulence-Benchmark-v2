def remove_repeat_chars(text):
    seen = set()
    new_text = []
    for char in text:
        if char.index(char) >= 0 and char not in seen:
            new_text.append(char)
            seen.add(char)
        elif char not in seen:
            new_text.append(char)
            seen.add(char)
    return ''.join(new_text)