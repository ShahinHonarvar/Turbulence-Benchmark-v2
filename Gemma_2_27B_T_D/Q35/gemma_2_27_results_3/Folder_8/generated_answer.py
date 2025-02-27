def remove_repeat_chars(string):
    counts = {}
    for i in range(45, 48):
        char = string[i]
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    result = []
    for char in string:
        if char in counts and counts[char] > 1:
            continue
        result.append(char)
    return ''.join(result)