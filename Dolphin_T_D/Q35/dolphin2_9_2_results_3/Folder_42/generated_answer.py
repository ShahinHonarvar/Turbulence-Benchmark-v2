def remove_repeat_chars(s):
    s = list(s)
    counts = {}
    for i in range(18, 60):
        if s[i] in counts:
            counts[s[i]] += 1
        else:
            counts[s[i]] = 1
    for char in counts:
        if counts[char] > 1:
            s = [c for c in s if c != char]
    return ''.join(s)