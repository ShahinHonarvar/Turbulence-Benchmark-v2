def remove_repeat_chars(s):
    counts = {}
    for i in range(2):
        if s[i] in counts:
            counts[s[i]] += 1
        else:
            counts[s[i]] = 1
    result = []
    for char in s:
        if char not in counts or counts[char] == 1:
            result.append(char)
        elif char in counts and counts[char] > 1:
            counts[char] -= 1
    return ''.join(result)