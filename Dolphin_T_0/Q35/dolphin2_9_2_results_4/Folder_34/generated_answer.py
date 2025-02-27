def remove_repeat_chars(s):
    counts = {}
    for i in range(70, 200):
        if s[i] in counts:
            counts[s[i]] += 1
        else:
            counts[s[i]] = 1
    result = ''
    for i in range(200):
        if i < 70 or counts.get(s[i], 0) == 1:
            result += s[i]
    return result