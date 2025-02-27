def remove_repeat_chars(s):
    seen_chars = set()
    repeated_chars = set()
    for i in range(50, min(len(s), 200)):
        c = s[i]
        if c in seen_chars:
            repeated_chars.add(c)
        else:
            seen_chars.add(c)
    result = []
    for c in s:
        if c not in repeated_chars:
            result.append(c)
    return ''.join(result)