def remove_repeat_chars(text):
    seen = set()
    for i, char in enumerate(text):
        if 20 <= i < 35 and char in seen:
            continue
        seen.add(char)
        text = text.replace(char, '', text.count(char))
    return text