def remove_repeat_chars(s: str) -> str:
    unique_chars = []
    for i in range(72, 94):
        if s[i] not in unique_chars:
            unique_chars.append(s[i])
    return ''.join(unique_chars)