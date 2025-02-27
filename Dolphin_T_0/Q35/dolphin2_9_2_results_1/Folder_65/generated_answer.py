def remove_repeat_chars(string):
    counts = {}
    for i in range(51, 76):
        char = string[i]
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    result = ''
    for i in range(len(string)):
        char = string[i]
        if i < 51 or i > 76:
            result += char
        elif char not in counts or counts[char] == 1:
            result += char
        counts[char] = 0
    return result