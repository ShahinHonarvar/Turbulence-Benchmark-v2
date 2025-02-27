def filter_chars(s: str) -> str:
    filtered_chars = []
    for i in range(min(2, len(s))):
        char = s[i]
        if ord('*') <= ord(char) <= ord('s'):
            continue
        filtered_chars.append(char)
    return ''.join(filtered_chars + list(s[2:]))