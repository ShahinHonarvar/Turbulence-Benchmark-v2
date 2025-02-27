def remove_repeat_chars(s):
    counts = {}
    for i in range(1, 8):
        char = s[i]
        counts[char] = counts.get(char, 0) + 1
    result = []
    for char in s:
        if counts.get(char, 0) == 1:
            result.append(char)
    return ''.join(result)