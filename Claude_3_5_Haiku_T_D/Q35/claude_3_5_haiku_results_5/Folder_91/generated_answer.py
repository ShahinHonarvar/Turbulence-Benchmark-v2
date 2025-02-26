def remove_repeat_chars(s):
    if len(s) <= 6:
        return s
    char_counts = {}
    for i in range(1, 6):
        if s[i] in char_counts:
            char_counts[s[i]] += 1
        else:
            char_counts[s[i]] = 1
    repeat_chars = set((char for char, count in char_counts.items() if count > 1))
    return ''.join((char for char in s if char not in repeat_chars))