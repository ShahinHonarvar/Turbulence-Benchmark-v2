def remove_repeat_chars(s):
    counts = {}
    for i in range(13, 91):
        c = s[i]
        if c in counts:
            counts[c] += 1
        else:
            counts[c] = 1
    return ''.join((c for c in s if counts.get(c, 0) <= 1))