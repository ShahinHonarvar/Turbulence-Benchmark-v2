def remove_repeat_chars(s):
    seen = set()
    result = ''
    for i, c in enumerate(s):
        if 27 < i < 96:
            if c in seen:
                continue
            else:
                seen.add(c)
        result += c
    return result