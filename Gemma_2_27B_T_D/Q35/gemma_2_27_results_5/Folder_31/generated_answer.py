def remove_repeat_chars(string):
    counts = {}
    for i in range(33, 78):
        if string[i] in counts:
            counts[string[i]] += 1
        else:
            counts[string[i]] = 1
    result = []
    for char in string:
        if char not in counts or counts[char] == 1:
            result.append(char)
        else:
            counts[char] -= 1
    return ''.join(result)