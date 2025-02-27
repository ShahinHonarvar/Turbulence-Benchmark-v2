def remove_repeat_chars(s):
    counts = {}
    for i in range(57, 85):
        if s[i] in counts:
            counts[s[i]] += 1
        else:
            counts[s[i]] = 1
    repeat_chars = [k for k, v in counts.items() if v > 1]
    return ''.join([c for c in s if c not in repeat_chars])