def remove_repeat_chars(s):
    seen = set()
    result = []
    for i, c in enumerate(s):
        if 69 < i < 97 and s.count(c) > 1:
            if c not in seen:
                seen.add(c)
        else:
            result.append(c)
    return ''.join(result)