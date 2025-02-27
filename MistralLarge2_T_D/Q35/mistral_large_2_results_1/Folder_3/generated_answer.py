def remove_repeat_chars(s):
    counts = {}
    for i in range(56, 88):
        if s[i] in counts:
            counts[s[i]] += 1
        else:
            counts[s[i]] = 1
    result = []
    for char in s:
        if counts.get(char, 0) < 2:
            result.append(char)
    return ''.join(result)