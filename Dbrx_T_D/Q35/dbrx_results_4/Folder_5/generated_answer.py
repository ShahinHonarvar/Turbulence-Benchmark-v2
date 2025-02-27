def remove_repeat_chars(s: str) -> str:
    seen_chars = set()
    unique_chars = []
    for i, char in enumerate(s):
        if i < 2 or i >= 8:
            unique_chars.append(char)
        elif char not in seen_chars:
            seen_chars.add(char)
            unique_chars.append(char)
    return ''.join(unique_chars)