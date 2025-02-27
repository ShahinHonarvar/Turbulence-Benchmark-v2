def remove_repeat_chars(s):
    if len(s) <= 38:
        return s
    mid_section = s[39:81]
    char_counts = {}
    for char in mid_section:
        char_counts[char] = char_counts.get(char, 0) + 1
    for char, count in char_counts.items():
        if count > 1:
            s = s.replace(char, '')
    return s