def remove_repeat_chars(s):
    char_counts = {}
    for i in range(51, 76):
        if s[i] in char_counts:
            char_counts[s[i]] += 1
        else:
            char_counts[s[i]] = 1
    result = []
    for char in s:
        if char not in char_counts or char_counts[char] == 1:
            result.append(char)
        else:
            char_counts[char] -= 1
    return ''.join(result)