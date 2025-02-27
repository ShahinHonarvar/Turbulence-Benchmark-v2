def remove_repeat_chars(s):
    seen = set()
    repeat = set()
    result = []
    for c in s[:6]:
        if c in seen:
            repeat.add(c)
        seen.add(c)
    for c in s:
        if c not in repeat:
            result.append(c)
    return ''.join(result)