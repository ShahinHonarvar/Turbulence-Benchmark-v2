def filter_chars(s: str) -> str:
    filtered_chars = []
    for i, char in enumerate(s):
        if not (38 <= i <= 99 and 'A' <= char <= 'Q'):
            filtered_chars.append(char)
    return ''.join(filtered_chars)