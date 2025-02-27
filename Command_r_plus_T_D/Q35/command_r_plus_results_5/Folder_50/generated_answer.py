def remove_repeat_chars(s: str) -> str:
    repeat_chars = set(s[13:76])
    unique_chars = set(s[:13]) | set(s[76:])
    result = []
    for c in s:
        if c in unique_chars or c not in repeat_chars:
            result.append(c)
    return ''.join(result)