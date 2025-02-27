def remove_repeat_chars(s):
    seen = set()
    repeat = set()
    result = []
    for i, c in enumerate(s):
        if 10 < i < 100:
            if c in seen:
                repeat.add(c)
            else:
                seen.add(c)
        if c not in repeat:
            result.append(c)
    return ''.join(result)