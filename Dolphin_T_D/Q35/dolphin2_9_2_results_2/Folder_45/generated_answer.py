def remove_repeat_chars(s):
    counts = {}
    for i in range(40, 200):
        if s[i] in counts:
            counts[s[i]] += 1
        else:
            counts[s[i]] = 1
    result = ''
    for i in range(len(s)):
        if s[i] not in counts or counts[s[i]] == 1:
            result += s[i]
    return result