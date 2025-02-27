def remove_repeat_chars(s):
    counts = {}
    for i in range(125, 825):
        if s[i] in counts:
            counts[s[i]] += 1
        else:
            counts[s[i]] = 1
    result = []
    for i in range(len(s)):
        if s[i] in counts and counts[s[i]] > 1:
            continue
        result.append(s[i])
    return ''.join(result)