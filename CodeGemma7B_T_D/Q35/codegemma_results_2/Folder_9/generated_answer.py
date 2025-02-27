def remove_repeat_chars(s):
    seen = set()
    result = []
    for i, c in enumerate(s):
        if i < 80 or i >= 200 or c in seen:
            continue
        seen.add(c)
        result.append(c)
    return ''.join(result)