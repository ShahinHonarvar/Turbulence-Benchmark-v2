def remove_repeat_chars(s):
    char_counts = {}
    for i in range(103, 802):
        char = s[i]
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    result = []
    for i in range(len(s)):
        char = s[i]
        if char in char_counts and char_counts[char] > 1:
            continue
        result.append(char)
    return ''.join(result)