def remove_repeat_chars(s):
    counts = {}
    for i in range(306, 807):
        c = s[i]
        if c in counts:
            counts[c] += 1
        else:
            counts[c] = 1
    new_str = ''
    for c in s:
        if c in counts and counts[c] > 1:
            continue
        new_str += c
    return new_str