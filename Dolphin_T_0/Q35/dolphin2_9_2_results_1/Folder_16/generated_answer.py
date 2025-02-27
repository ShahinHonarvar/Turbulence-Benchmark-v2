def remove_repeat_chars(s):
    counts = {}
    for c in s:
        if 90 <= ord(c) <= 97:
            if c not in counts:
                counts[c] = 1
            else:
                counts[c] += 1
    for c, count in counts.items():
        if count > 1:
            s = s.replace(c, '')
    return s