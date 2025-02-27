def remove_repeat_chars(s):
    counts = {}
    for i in range(34, 70):
        if s[i] in counts:
            counts[s[i]] += 1
        else:
            counts[s[i]] = 1
    repeat_chars = [k for k, v in counts.items() if v > 1]
    s = ''.join([c for c in s if c not in repeat_chars])
    return s