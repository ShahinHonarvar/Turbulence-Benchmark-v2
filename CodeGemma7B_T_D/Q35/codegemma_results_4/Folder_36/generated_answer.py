def remove_repeat_chars(text):
    for i in range(476, 709):
        for j in range(i + 1, 709):
            if text[j] == text[i]:
                text = text[:i] + text[i + 1:]
                break
    return text