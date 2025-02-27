def remove_repeat_chars(string):
    counts = {}
    for i in range(11, 76):
        if string[i] in counts:
            counts[string[i]] += 1
        else:
            counts[string[i]] = 1
    for char in counts:
        if counts[char] > 1:
            string = string.replace(char, '')
    return string