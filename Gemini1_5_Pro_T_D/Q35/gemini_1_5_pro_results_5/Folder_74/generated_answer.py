def remove_repeat_chars(s):
    seen = set()
    result = []
    for i, c in enumerate(s):
        if 69 < i < 97:
            if c in seen:
                continue
            elif s[69:97].count(c) > 1:
                seen.add(c)
                continue
        result.append(c)
    return ''.join(result)