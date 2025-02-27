def remove_repeat_chars(s):
    char_counts = {}
    for i in range(10, 100):
        if s[i] in char_counts:
            char_counts[s[i]] += 1
        else:
            char_counts[s[i]] = 1
    result = []
    for char in s:
        if char_counts.get(char, 0) <= 1:
            result.append(char)
    return ''.join(result)