def remove_repeat_chars(text):
    for i in range(81, 86):
        for j in range(i + 1, 86):
            while text[j] == text[i]:
                text = text[:j] + text[j + 1:]
    return text