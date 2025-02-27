def remove_repeat_chars(text):
    for i in range(20, 36):
        for j in range(i + 1, len(text)):
            if text[i] == text[j]:
                text = text[:i] + text[i + 1:]
                break
    return text