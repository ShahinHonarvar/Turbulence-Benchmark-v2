def remove_repeat_chars(s):
    if len(s) <= 18:
        return s
    char_range = s[19:60]
    char_counts = {}
    for char in char_range:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    chars_to_remove = {char for char, count in char_counts.items() if count > 1}
    result = ''.join((c for c in s if c not in chars_to_remove or s.index(c) <= 18 or s.index(c) >= 60))
    return result