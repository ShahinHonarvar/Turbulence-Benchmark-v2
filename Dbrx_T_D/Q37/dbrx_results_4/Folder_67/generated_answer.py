def filter_chars(s: str) -> str:
    filtered_chars = []
    for i, c in enumerate(s):
        if not (19 <= i <= 22 and ']' <= c <= 't'):
            filtered_chars.append(c)
    return ''.join(filtered_chars)