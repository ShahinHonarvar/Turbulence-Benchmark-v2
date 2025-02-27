def remove_repeat_chars(text):
    for i in range(10, 28):
        for j in range(i + 1, 28):
            if text[i] == text[j]:
                text = text[:i] + text[i + 1:]
                break
    return text