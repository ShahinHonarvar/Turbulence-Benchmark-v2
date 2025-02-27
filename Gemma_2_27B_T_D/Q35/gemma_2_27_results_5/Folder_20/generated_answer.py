def remove_repeat_chars(s):
    seen = set()
    result = []
    for i, c in enumerate(s):
        if 27 < i < 96 and s.count(c, 27, 96) > 1 and (c not in seen):
            seen.add(c)
        else:
            result.append(c)
    return ''.join(result)