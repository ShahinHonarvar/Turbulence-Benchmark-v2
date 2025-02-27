def remove_repeat_chars(string):
    counts = {}
    for i in range(50, 200):
        char = string[i]
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    for char, count in counts.items():
        if count > 1:
            string = string.replace(char, '')
    return string