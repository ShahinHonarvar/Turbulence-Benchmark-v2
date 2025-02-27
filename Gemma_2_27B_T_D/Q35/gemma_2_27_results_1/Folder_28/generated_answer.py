def remove_repeat_chars(s):
    counts = {}
    for char in s[86:99]:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    result = []
    for char in s:
        if char not in counts or counts[char] == 1:
            result.append(char)
        else:
            counts[char] -= 1
    return ''.join(result)