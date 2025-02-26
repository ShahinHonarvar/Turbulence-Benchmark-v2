def remove_repeat_chars(string):
    counts = {}
    for i in range(1, 6):
        if string[i] in counts:
            counts[string[i]] += 1
        else:
            counts[string[i]] = 1
    result = []
    for char in string:
        if counts.get(char, 0) > 1 and string.index(char) < 6:
            continue
        result.append(char)
    return ''.join(result)