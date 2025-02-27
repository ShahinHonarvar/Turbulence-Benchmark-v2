def remove_repeat_chars(string):
    counts = {}
    for i in range(355, 988):
        char = string[i]
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    result = []
    for char in string:
        if char not in counts or counts[char] == 1:
            result.append(char)
        else:
            counts[char] -= 1
    return ''.join(result)