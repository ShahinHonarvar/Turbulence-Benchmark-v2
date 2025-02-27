def filter_chars(s: str) -> str:
    filtered_chars = []
    for i, char in enumerate(s):
        if i < 43 or i >= 69:
            filtered_chars.append(char)
        elif char > 'B' and char < 'r' and (char not in filtered_chars):
            filtered_chars.append(char)
    return ''.join(filtered_chars)