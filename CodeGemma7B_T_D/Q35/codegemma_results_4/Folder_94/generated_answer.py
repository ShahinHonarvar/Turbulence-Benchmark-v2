def remove_repeat_chars(s):
    seen = set()
    new_s = []
    for i, c in enumerate(s):
        if i < 42 or i >= 87 or c not in seen:
            seen.add(c)
            new_s.append(c)
    return ''.join(new_s)