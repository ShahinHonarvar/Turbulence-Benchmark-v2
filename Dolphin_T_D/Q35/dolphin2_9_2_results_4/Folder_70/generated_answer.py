def remove_repeat_chars(s):
    counts = {}
    for i in range(43, 70):
        if s[i] not in counts and s.count(s[i]) > 1:
            counts[s[i]] = True
    return ''.join((char for char in s if char not in counts))