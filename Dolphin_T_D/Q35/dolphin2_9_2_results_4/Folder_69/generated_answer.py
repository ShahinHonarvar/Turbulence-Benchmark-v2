def remove_repeat_chars(string):
    counts = {}
    for i in range(39, 43):
        if string[i] not in counts:
            counts[string[i]] = 1
        else:
            counts[string[i]] += 1
    for char, count in counts.items():
        if count > 1:
            string = string.replace(char, '')
    return string