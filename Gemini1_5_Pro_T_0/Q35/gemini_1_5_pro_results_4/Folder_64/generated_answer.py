def remove_repeat_chars(s):
    seen = set()
    repeated = set()
    for i in range(1, len(s) - 1):
        if i < 5:
            if s[i] in seen:
                repeated.add(s[i])
            else:
                seen.add(s[i])
    keep = []
    for c in s:
        if c not in repeated:
            keep.append(c)
    return ''.join(keep)