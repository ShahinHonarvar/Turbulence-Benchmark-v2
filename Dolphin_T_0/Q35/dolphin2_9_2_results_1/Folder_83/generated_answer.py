def remove_repeat_chars(s):
    counts = {}
    for i in range(100, 200):
        if s[i] in counts:
            counts[s[i]] += 1
        else:
            counts[s[i]] = 1
    chars_to_remove = [k for k, v in counts.items() if v > 1]
    new_s = ''.join([c for c in s if c not in chars_to_remove])
    return new_s