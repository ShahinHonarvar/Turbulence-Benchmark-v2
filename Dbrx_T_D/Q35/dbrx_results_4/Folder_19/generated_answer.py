def remove_repeat_chars(s: str) -> str:
    seen_chars = set()
    unique_chars = []
    for i, char in enumerate(s):
        if i >= 1 and i < 4:
            if char in seen_chars:
                continue
            else:
                seen_chars.add(char)
        unique_chars.append(char)
    return ''.join(unique_chars)