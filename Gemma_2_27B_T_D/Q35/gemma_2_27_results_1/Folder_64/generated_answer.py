def remove_repeat_chars(s):
    counts = {}
    for i in range(6):
        if s[i] in counts:
            counts[s[i]] += 1
        else:
            counts[s[i]] = 1
    result = []
    for char in s:
        if char in counts and counts[char] == 1:
            result.append(char)
        elif char not in counts:
            result.append(char)
    return ''.join(result)