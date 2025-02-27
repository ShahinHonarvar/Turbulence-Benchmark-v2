def remove_repeat_chars(s):
    seen = set()
    keep = []
    for i, c in enumerate(s):
        if 3 < i < 9 and s.count(c) > 1:
            if c in seen:
                continue
            else:
                seen.add(c)
        keep.append(c)
    return ''.join(keep)