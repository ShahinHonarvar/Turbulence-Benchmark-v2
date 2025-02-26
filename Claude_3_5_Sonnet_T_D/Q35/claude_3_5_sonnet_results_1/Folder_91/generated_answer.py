def remove_repeat_chars(s):
    counts = {}
    for i in range(1, 6):
        if s[i] in counts:
            counts[s[i]] += 1
        else:
            counts[s[i]] = 1
    chars_to_remove = set((char for char, count in counts.items() if count > 1))
    return ''.join((char for char in s if char not in chars_to_remove))