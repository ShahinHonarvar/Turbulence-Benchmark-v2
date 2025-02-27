def remove_repeat_chars(s):
    if len(s) <= 11:
        return s
    mid_section = s[11:28]
    char_counts = {}
    for char in mid_section:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    repeated_chars = {char for char, count in char_counts.items() if count > 1}
    return ''.join((char for char in s if char not in repeated_chars or s.index(char) >= 28 or s.index(char) < 11))