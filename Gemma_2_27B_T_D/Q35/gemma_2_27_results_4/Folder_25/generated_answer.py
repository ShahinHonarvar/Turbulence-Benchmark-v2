def remove_repeat_chars(s):
    counts = {}
    for i in range(37, 43):
        if i < len(s) and s[i] in counts:
            counts[s[i]] += 1
        elif i < len(s):
            counts[s[i]] = 1
    result = []
    for char in s:
        if char not in counts or counts[char] == 1:
            result.append(char)
    return ''.join(result)