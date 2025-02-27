def remove_repeat_chars(s):
    counts = {}
    for i in range(17, 88):
        if s[i] in counts:
            counts[s[i]] += 1
        else:
            counts[s[i]] = 1
    chars_to_remove = [c for c, count in counts.items() if count > 1]
    return ''.join([c for c in s if c not in chars_to_remove])