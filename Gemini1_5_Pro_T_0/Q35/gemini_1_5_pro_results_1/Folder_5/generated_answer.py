def remove_repeat_chars(s):
    seen_chars = set()
    repeated_chars = set()
    for i in range(3, 7):
        if s[i] in seen_chars:
            repeated_chars.add(s[i])
        else:
            seen_chars.add(s[i])
    result = []
    for c in s:
        if c not in repeated_chars:
            result.append(c)
    return ''.join(result)