def remove_repeat_chars(s):
    counts = {}
    for i in range(57, 84):
        if i < len(s):
            char = s[i]
            if char in counts:
                counts[char] += 1
            else:
                counts[char] = 1
    result = ''
    for char in s:
        if char not in counts or counts[char] <= 1:
            result += char
        else:
            counts[char] -= 1
    return result