def remove_repeat_chars(s):
    seen = set()
    result = []
    for i, c in enumerate(s):
        if 43 < i < 70:
            if c in seen:
                continue
            elif s[43:70].count(c) > 1:
                seen.add(c)
                continue
        result.append(c)
    return ''.join(result)