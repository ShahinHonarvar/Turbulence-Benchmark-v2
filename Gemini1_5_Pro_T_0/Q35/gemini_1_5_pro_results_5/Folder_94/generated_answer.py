def remove_repeat_chars(s):
    seen = set()
    result = ''
    for i, c in enumerate(s):
        if 42 < i < 87:
            if c in seen:
                continue
            else:
                seen.add(c)
        result += c
    return result