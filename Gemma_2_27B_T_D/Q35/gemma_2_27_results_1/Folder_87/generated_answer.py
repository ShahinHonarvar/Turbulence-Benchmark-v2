def remove_repeat_chars(s):
    counts = {}
    for i in range(20, 43):
        if s[i] in counts:
            counts[s[i]] += 1
        else:
            counts[s[i]] = 1
    result = []
    for c in s:
        if c in counts and counts[c] > 1:
            continue
        result.append(c)
    return ''.join(result)