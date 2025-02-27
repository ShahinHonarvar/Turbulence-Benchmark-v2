def filter_chars(s: str) -> str:
    filtered_chars = []
    for i, char in enumerate(s):
        if not (26 <= i <= 64 and 'V' <= char <= 'o'):
            filtered_chars.append(char)
    return ''.join(filtered_chars)