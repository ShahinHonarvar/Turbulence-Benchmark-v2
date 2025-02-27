def remove_repeat_chars(s):
    seen = set()
    keep = []
    for i, c in enumerate(s):
        if 46 < i < 91:
            if c in seen:
                continue
            else:
                seen.add(c)
        keep.append(c)
    return ''.join(keep)