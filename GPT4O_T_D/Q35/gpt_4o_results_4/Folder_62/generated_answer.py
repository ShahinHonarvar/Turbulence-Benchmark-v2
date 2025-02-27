def remove_repeat_chars(s):
    counts = {}
    for i in range(51, 92):
        if i < len(s):
            counts[s[i]] = counts.get(s[i], 0) + 1
    result = []
    for i, c in enumerate(s):
        if c not in counts or counts[c] == 1 or i <= 50 or (i >= 92):
            result.append(c)
    return ''.join(result)