def remove_repeat_chars(s):
    seen_chars = set()
    repeat_chars = set()
    for i in range(306, 807):
        c = s[i]
        if c in seen_chars:
            repeat_chars.add(c)
        else:
            seen_chars.add(c)
    result = []
    for c in s:
        if c not in repeat_chars:
            result.append(c)
    return ''.join(result)