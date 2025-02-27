def remove_repeat_chars(s):
    counts = {}
    for i in range(90, 200):
        if s[i] not in counts:
            counts[s[i]] = 1
        else:
            counts[s[i]] += 1
    result = ''
    for i in range(len(s)):
        if i < 90 or i >= 200 or counts.get(s[i], 0) == 1:
            result += s[i]
    return result