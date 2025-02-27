def remove_repeat_chars(s):
    counts = {}
    for c in s[50:200]:
        if c in counts:
            counts[c] += 1
        else:
            counts[c] = 1
    result = ''
    for c in s:
        if c not in counts or counts[c] == 1:
            result += c
    return result