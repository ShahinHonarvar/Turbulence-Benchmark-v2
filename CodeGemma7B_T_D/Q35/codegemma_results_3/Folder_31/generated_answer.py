def remove_repeat_chars(s):
    seen = set()
    result = []
    for i, c in enumerate(s):
        if 33 < i < 78 and c not in seen:
            seen.add(c)
            result.append(c)
    return ''.join(result)