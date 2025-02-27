def remove_repeat_chars(s):
    char_counts = {}
    for i in range(36, 85):
        if s[i] in char_counts:
            char_counts[s[i]] += 1
        else:
            char_counts[s[i]] = 1
    result = []
    for char in s:
        if char in char_counts and char_counts[char] > 1:
            continue
        result.append(char)
    return ''.join(result)