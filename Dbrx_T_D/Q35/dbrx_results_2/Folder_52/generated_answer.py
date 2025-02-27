def remove_repeat_chars(s: str) -> str:
    unique_chars = []
    for i in range(38, 81):
        if s[i] not in s[:i] + s[i + 1:]:
            unique_chars.append(s[i])
    return ''.join(unique_chars)