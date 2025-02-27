def remove_repeat_chars(string):
    counts = {}
    for char in string[10:28]:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    for char, count in counts.items():
        if count > 1:
            string = string.replace(char, '')
    return string