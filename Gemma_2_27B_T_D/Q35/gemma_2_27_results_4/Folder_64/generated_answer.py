def remove_repeat_chars(s):
    counts = {}
    for i in range(len(s)):
        if i >= 0 and i < 5:
            if s[i] in counts:
                counts[s[i]] += 1
            else:
                counts[s[i]] = 1
    result = []
    for c in s:
        if c not in counts or counts[c] == 1:
            result.append(c)
    return ''.join(result)