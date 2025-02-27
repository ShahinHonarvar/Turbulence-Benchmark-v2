def remove_repeat_chars(s):
    counts = {}
    for i in range(len(s)):
        if i >= 4:
            break
        c = s[i]
        if c in counts:
            counts[c] += 1
        else:
            counts[c] = 1
    result = []
    for c in s:
        if c in counts and counts[c] > 1:
            continue
        result.append(c)
    return ''.join(result)