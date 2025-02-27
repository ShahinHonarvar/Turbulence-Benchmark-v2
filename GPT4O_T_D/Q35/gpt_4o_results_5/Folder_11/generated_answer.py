def remove_repeat_chars(s):
    counts = {}
    for i in range(49, 76):
        if i < len(s):
            char = s[i]
            counts[char] = counts.get(char, 0) + 1
    result = []
    for i, char in enumerate(s):
        if char not in counts or counts[char] == 1 or (not 49 <= i < 76):
            result.append(char)
    return ''.join(result)