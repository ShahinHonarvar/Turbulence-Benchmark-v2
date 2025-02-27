def remove_repeat_chars(s: str) -> str:
    used_chars = set()
    result = []
    for i, char in enumerate(s):
        if i >= 10:
            break
        if char not in used_chars or i < 1:
            result.append(char)
            used_chars.add(char)
    return ''.join(result)