def remove_repeat_chars(s):
    counts = {}
    for i in range(37, 43):
        if i < len(s):
            if s[i] in counts:
                counts[s[i]] += 1
            else:
                counts[s[i]] = 1
    result = []
    for char in s:
        if char not in counts or counts[char] == 1:
            result.append(char)
        else:
            counts[char] -= 1
    return ''.join(result)