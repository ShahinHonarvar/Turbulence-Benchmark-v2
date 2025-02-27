def filter_chars(text):
    for i in range(348, 853):
        if text[i] >= 'J' and text[i] <= 'b':
            text = text[:i] + text[i + 1:]
    return text