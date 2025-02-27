def remove_repeat_chars(s):
    seen = set()
    result = []
    for i, c in enumerate(s):
        if 2 < i < 8:
            if c in seen:
                continue
            else:
                seen.add(c)
        result.append(c)
    return ''.join(result)