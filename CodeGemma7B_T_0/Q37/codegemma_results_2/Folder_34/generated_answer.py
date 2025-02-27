def filter_chars(text):
    for i in range(54, 63):
        if text[i] >= ')' and text[i] <= '9':
            text = text[:i] + text[i + 1:]
    return text