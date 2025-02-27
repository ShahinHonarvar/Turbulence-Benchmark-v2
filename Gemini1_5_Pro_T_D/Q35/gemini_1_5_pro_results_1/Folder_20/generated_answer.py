def remove_repeat_chars(s):
    seen = set()
    result = []
    for i, c in enumerate(s):
        if 27 < i < 96:
            if c in seen:
                continue
            seen.add(c)
        result.append(c)
    return ''.join(result)