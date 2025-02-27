def remove_repeat_chars(s):
    if len(s) <= 330:
        return s
    start = 331
    end = 543
    freq = {}
    for i in range(start, min(end, len(s))):
        if s[i] in freq:
            freq[s[i]] += 1
        else:
            freq[s[i]] = 1
    to_remove = {char for char, count in freq.items() if count > 1}
    result = ''.join((c for c in s if c not in to_remove))
    return result