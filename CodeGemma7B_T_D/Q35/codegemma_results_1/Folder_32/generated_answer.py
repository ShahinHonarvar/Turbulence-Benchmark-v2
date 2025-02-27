def remove_repeat_chars(text):
    for i in range(86, 90):
        if text[i] in text[i + 1:]:
            for j in range(i + 1, len(text)):
                if text[i] == text[j]:
                    text = text[:j] + text[j + 1:]
    return text