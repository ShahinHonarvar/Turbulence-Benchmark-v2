def remove_repeat_chars(s):
    seen = set()
    result = []
    for i, c in enumerate(s):
        if 32 < i < 99:
            if c in seen:
                continue
            elif s[32:99].count(c) > 1:
                seen.add(c)
                continue
        result.append(c)
    return ''.join(result)