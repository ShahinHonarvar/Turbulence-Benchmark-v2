def remove_repeat_chars(s):
    seen = set()
    result = []
    for i, c in enumerate(s):
        if 42 < i < 87 and c in seen:
            continue
        seen.add(c)
        result.append(c)
    return ''.join(result)