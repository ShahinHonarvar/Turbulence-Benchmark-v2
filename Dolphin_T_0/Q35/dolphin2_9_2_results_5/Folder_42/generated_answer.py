def remove_repeat_chars(s):
    char_counts = {}
    for i in range(18, 60):
        if s[i] in char_counts:
            char_counts[s[i]] += 1
        else:
            char_counts[s[i]] = 1
    for char in char_counts:
        if char_counts[char] > 1:
            s = s.replace(char, '')
    return s