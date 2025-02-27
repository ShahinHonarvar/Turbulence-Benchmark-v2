def filter_chars(text: str) -> str:
    filtered = text
    for char_code in range(36, 60):
        char = chr(char_code)
        if '!' < char.upper() < 'B':
            filtered = filtered.replace(char, '')
    return filtered