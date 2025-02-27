def remove_repeat_chars(s):
    counts = {}
    for i in range(29, 53):
        if s[i] in counts:
            counts[s[i]] += 1
        else:
            counts[s[i]] = 1
    result = []
    for i in range(len(s)):
        if s[i] not in counts or counts[s[i]] == 1:
            result.append(s[i])
        else:
            counts[s[i]] -= 1
    return ''.join(result)