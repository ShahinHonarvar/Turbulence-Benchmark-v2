def remove_repeat_chars(s):
    counts = {}
    for i in range(1, 7):
        if s[i] in counts:
            counts[s[i]] += 1
        else:
            counts[s[i]] = 1
    return ''.join((c for c in s if not (c in counts and counts[c] > 1)))