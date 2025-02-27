def remove_repeat_chars(text):
    for i in range(1, 4):
        for j in range(i + 1, 4):
            if text[i] == text[j]:
                text = text[:i] + text[i + 1:]
    return text