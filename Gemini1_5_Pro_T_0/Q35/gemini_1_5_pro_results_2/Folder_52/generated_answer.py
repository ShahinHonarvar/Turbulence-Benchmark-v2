def remove_repeat_chars(s):
    seen = set()
    keep = []
    for i, c in enumerate(s):
        if 38 < i < 81:
            if c in seen:
                continue
            else:
                seen.add(c)
        keep.append(c)
    return ''.join(keep)