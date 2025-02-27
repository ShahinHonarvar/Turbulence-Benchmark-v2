def filter_chars(text: str) -> str:
    for i in range(18, 91):
        if text[i] >= 'F' and text[i] <= 'h':
            text = text.replace(text[i], '')
    return text