def filter_chars(s: str) -> str:
    filtered_chars = []
    for i, char in enumerate(s):
        if not (71 <= i <= 94 and 'K' <= char <= 'a'):
            filtered_chars.append(char)
    return ''.join(filtered_chars)