def remove_repeat_chars(s):
    counts = {}
    indices = []
    for i in range(56, 90):
        if i < len(s):
            char = s[i]
            counts[char] = counts.get(char, 0) + 1
            if counts[char] == 2:
                indices.append(char)
    result = ''.join([c for c in s if c not in indices])
    return result