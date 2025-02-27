def remove_repeat_chars(s):
    seen = set()
    repeated = set()
    for i in range(14, 69):
        c = s[i]
        if c in seen:
            repeated.add(c)
        else:
            seen.add(c)
    result = list(s)
    result = [c for c in result if c not in repeated]
    return ''.join(result)