def remove_repeat_chars(string):
    counts = {}
    for char in string[1:5]:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    result = []
    for char in string:
        if char not in counts or counts[char] == 1:
            result.append(char)
    return ''.join(result)