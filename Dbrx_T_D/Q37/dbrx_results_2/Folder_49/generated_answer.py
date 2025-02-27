def filter_chars(s: str) -> str:
    filtered_chars = []
    for i, char in enumerate(s):
        if 42 <= ord(char) <= 98 and 42 <= i <= 97:
            continue
        filtered_chars.append(char)
    return ''.join(filtered_chars)