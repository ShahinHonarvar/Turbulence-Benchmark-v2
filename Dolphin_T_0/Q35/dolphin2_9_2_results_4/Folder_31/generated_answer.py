def remove_repeat_chars(s):
    s = list(s)
    indices = []
    for i in range(33, 78):
        counts = s.count(s[i])
        if counts > 1:
            indices.append(i)
    indices = set(indices)
    for i in sorted(indices, reverse=True):
        del s[i]
    return ''.join(s)