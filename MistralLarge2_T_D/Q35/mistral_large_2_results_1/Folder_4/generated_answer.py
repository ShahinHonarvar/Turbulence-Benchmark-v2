def remove_repeat_chars(s):
    counts = {}
    for i in range(49, 75):
        if i < len(s):
            if s[i] in counts:
                counts[s[i]] += 1
            else:
                counts[s[i]] = 1
    result = [c for c in s if counts.get(c, 0) <= 1]
    return ''.join(result)