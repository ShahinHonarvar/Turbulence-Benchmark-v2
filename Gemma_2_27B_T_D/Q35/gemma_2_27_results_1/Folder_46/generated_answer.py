def remove_repeat_chars(s):
    char_counts = {}
    for i in range(10, 79):
        char = s[i]
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    result = []
    for c in s:
        if c not in char_counts or char_counts[c] == 1:
            result.append(c)
    return ''.join(result)