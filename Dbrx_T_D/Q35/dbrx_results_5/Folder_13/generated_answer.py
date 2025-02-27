def remove_repeat_chars(s: str) -> str:
    used_chars = set()
    result = []
    for i, char in enumerate(s):
        if 46 < i < 91 and char in used_chars:
            continue
        if i not in [46, 91]:
            used_chars.add(char)
        result.append(char)
    return ''.join(result)