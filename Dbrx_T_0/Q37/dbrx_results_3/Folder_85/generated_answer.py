def filter_chars(s: str) -> str:
    filtered_chars = []
    for i, char in enumerate(s):
        if not (28 <= i <= 65 and 'O' <= char <= 'd'):
            filtered_chars.append(char)
    return ''.join(filtered_chars)