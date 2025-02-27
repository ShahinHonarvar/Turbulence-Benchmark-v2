def remove_repeat_chars(s):
    seen = set()
    result = []
    for i, c in enumerate(s):
        if 13 < i < 91 and s.count(c) > 1:
            if c not in seen:
                seen.add(c)
            else:
                continue
        result.append(c)
    return ''.join(result)