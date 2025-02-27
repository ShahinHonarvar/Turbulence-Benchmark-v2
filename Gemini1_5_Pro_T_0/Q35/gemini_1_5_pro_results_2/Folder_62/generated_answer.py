def remove_repeat_chars(s):
    seen = set()
    result = []
    for i, c in enumerate(s):
        if 50 < i < 92:
            if c in seen:
                continue
            elif s.count(c) > 1:
                seen.add(c)
                continue
        result.append(c)
    return ''.join(result)