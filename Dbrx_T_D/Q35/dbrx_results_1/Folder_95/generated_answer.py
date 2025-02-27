def remove_repeat_chars(s: str) -> str:
    used_chars = set()
    result = []
    for i, c in enumerate(s):
        if 32 < i < 99:
            if c in used_chars:
                continue
            else:
                used_chars.add(c)
        result.append(c)
    return ''.join(result)