def filter_chars(s: str) -> str:
    filtered_chars = []
    for i, char in enumerate(s):
        if not (19 <= i <= 32 and 'f' <= char <= 'o'):
            filtered_chars.append(char)
    return ''.join(filtered_chars)