def remove_repeat_chars(s: str) -> str:
    chars = []
    for i in range(25, 80):
        if s[i] not in chars:
            chars.append(s[i])
    result = ''.join(chars)
    return result