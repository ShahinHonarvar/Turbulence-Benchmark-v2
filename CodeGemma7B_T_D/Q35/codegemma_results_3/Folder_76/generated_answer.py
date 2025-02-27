def remove_repeat_chars(s):
    seen_chars = set()
    result = []
    for i, c in enumerate(s):
        if i >= 330 and i < 543 and (c in seen_chars):
            continue
        seen_chars.add(c)
        result.append(c)
    return ''.join(result)