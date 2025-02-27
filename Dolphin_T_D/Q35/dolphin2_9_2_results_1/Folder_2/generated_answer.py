def remove_repeat_chars(string):
    counts = {}
    for char in string[72:93]:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    for char in counts:
        if counts[char] > 1:
            string = string.replace(char, '')
    return string