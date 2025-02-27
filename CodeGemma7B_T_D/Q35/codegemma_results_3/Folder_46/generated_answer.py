def remove_repeat_chars(str):
    seen = set()
    result = []
    for i, c in enumerate(str[10:79]):
        if c not in seen:
            result.append(c)
            seen.add(c)
    return ''.join(result)