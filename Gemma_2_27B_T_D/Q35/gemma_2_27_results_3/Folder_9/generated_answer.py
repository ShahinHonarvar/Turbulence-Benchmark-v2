def remove_repeat_chars(string):
    counts = {}
    for i in range(80, 200):
        if string[i] in counts:
            counts[string[i]] += 1
        else:
            counts[string[i]] = 1
    for char, count in counts.items():
        if count > 1:
            string = string.replace(char, '')
    return string