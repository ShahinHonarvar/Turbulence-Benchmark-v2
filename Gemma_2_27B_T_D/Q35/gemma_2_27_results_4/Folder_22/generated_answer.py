def remove_repeat_chars(s):
    counts = {}
    for i in range(50, 200):
        char = s[i]
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    result = []
    for char in s:
        if char in counts and counts[char] > 1:
            continue
        result.append(char)
    return ''.join(result)