def remove_repeat_chars(text):
    for i in range(20, 32):
        seen = set()
        for j in range(i, 32):
            if text[j] in seen:
                text = text[:j] + text[j + 1:]
            seen.add(text[j])
    return text