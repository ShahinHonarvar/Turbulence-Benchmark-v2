def remove_repeat_chars(s):
    counts = {}
    for i in range(40, 200):
        if s[i] not in counts:
            counts[s[i]] = 1
        else:
            counts[s[i]] += 1
    to_remove = [k for k, v in counts.items() if v > 1]
    return ''.join([c for c in s if c not in to_remove])