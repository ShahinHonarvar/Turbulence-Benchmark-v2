def remove_repeat_chars(s):
    counts = {}
    for i in range(44, 91):
        if s[i] not in counts:
            counts[s[i]] = 1
        else:
            counts[s[i]] += 1
    repeat_chars = [k for k, v in counts.items() if v > 1]
    result = ''
    for i in range(len(s)):
        if s[i] not in repeat_chars:
            result += s[i]
    return result