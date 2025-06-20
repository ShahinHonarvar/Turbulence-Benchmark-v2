def remove_repeat_chars(s):
    char_counts = {}
    for i in range(57, 85):
        if i >= len(s):
            break
        char = s[i]
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    for char, count in char_counts.items():
        if count > 1:
            s = s.replace(char, '')
    return s