def remove_repeat_chars(s):
    if len(s) <= 76:
        return s
    mid_section = s[52:76]
    counts = {}
    for char in mid_section:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    repeated_chars = {char for char, count in counts.items() if count > 1}
    return ''.join((char for char in s if char not in repeated_chars or s.index(char) not in range(52, 76)))