def remove_repeat_chars(string):
    counts = {}
    for i in range(80, 200):
        if string[i] in counts:
            counts[string[i]] += 1
        else:
            counts[string[i]] = 1
    result = []
    for char in string:
        if char in counts and counts[char] > 1:
            continue
        result.append(char)
    return ''.join(result)