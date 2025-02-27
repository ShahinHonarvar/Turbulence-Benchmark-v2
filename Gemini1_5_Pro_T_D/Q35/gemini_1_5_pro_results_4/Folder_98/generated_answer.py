def remove_repeat_chars(s):
    seen = set()
    result = []
    for i, c in enumerate(s):
        if 0 < i < 7 and s.count(c) > 1:
            if c not in seen:
                seen.add(c)
                result.append(c)
        else:
            result.append(c)
    return ''.join(result)