def remove_repeat_chars(s):
    seen = set()
    keep = []
    for i, c in enumerate(s):
        if i > 13 and i < 91 and (s.count(c) > 1):
            if c not in seen:
                seen.add(c)
        else:
            keep.append(c)
    return ''.join(keep)