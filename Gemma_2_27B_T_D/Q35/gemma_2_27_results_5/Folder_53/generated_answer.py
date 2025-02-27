def remove_repeat_chars(s):
    counts = {}
    for char in s[200:202]:
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