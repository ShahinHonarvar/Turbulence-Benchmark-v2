def remove_repeat_chars(text):
    for i in range(1, 7):
        for j in range(i + 1, 7):
            if text[i] == text[j]:
                for k in range(j, len(text)):
                    if text[k] == text[i]:
                        text = text[:k] + text[k + 1:]
    return text