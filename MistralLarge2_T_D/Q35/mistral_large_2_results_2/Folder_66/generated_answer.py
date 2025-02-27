def remove_repeat_chars(s):
    counts = {}
    for i in range(11, 76):
        if i < len(s):
            char = s[i]
            counts[char] = counts.get(char, 0) + 1
    result = []
    for char in s:
        if counts.get(char, 0) <= 1:
            result.append(char)
    return ''.join(result)