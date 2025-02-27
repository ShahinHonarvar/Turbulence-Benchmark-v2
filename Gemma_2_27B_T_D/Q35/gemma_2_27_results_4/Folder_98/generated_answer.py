def remove_repeat_chars(s):
    counts = {}
    for i in range(8):
        if s[i] in counts:
            counts[s[i]] += 1
        else:
            counts[s[i]] = 1
    result = []
    for c in s:
        if counts.get(c, 0) <= 1:
            result.append(c)
    return ''.join(result)