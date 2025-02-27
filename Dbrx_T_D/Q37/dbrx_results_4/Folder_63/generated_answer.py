def filter_chars(s: str) -> str:
    filtered_chars = []
    for i, char in enumerate(s):
        if not (42 <= i <= 92 and '/' <= char <= 'a'):
            filtered_chars.append(char)
    return ''.join(filtered_chars)