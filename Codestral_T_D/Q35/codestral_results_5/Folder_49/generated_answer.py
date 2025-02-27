def remove_repeat_chars(s):
    counts = {}
    for i in range(90, 200):
        if i < len(s):
            counts[s[i]] = counts.get(s[i], 0) + 1
    return ''.join((c for c in s if counts.get(c, 0) <= 1))