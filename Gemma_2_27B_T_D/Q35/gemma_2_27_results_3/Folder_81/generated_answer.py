def remove_repeat_chars(s):
    char_counts = {}
    for i in range(20, 200):
        if s[i] in char_counts:
            char_counts[s[i]] += 1
        else:
            char_counts[s[i]] = 1
    for char, count in char_counts.items():
        if count > 1:
            s = s.replace(char, '')
    return s