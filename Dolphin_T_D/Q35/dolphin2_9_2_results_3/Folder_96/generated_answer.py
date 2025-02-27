def remove_repeat_chars(s):
    counts = {}
    result = ''
    for i in range(60, 200):
        if s[i] not in counts:
            counts[s[i]] = 1
        else:
            counts[s[i]] += 1
    for i in range(len(s)):
        if i < 60 or i >= 200 or counts.get(s[i], 0) < 2:
            result += s[i]
    return result