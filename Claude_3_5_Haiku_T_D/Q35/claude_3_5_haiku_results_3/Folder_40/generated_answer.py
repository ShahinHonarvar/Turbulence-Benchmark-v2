def remove_repeat_chars(s):
    if len(s) <= 3:
        return s
    seen = {}
    for i in range(1, 3):
        if s[i] in seen:
            seen[s[i]] += 1
        else:
            seen[s[i]] = 1
    repeat_chars = set((char for char, count in seen.items() if count > 1))
    return ''.join((char for char in s if char not in repeat_chars))