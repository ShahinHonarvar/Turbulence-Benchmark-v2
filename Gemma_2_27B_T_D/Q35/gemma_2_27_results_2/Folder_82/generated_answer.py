def remove_repeat_chars(s):
    seen = set()
    counts = {}
    for i in range(30, 200):
        char = s[i]
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    for char, count in counts.items():
        if count > 1:
            seen.add(char)
    result = []
    for char in s:
        if char not in seen:
            result.append(char)
    return ''.join(result)