def remove_repeat_chars(text):
    for i in range(7, 9):
        seen = set()
        for j in range(i + 1, len(text)):
            if text[j] != text[i] or text[j] in seen:
                continue
            seen.add(text[j])
            text = text[:j] + text[j + 1:]
    return text