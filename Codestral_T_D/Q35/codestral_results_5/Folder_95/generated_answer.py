def remove_repeat_chars(string):
    counts = {}
    result = ''
    for char in string[32:99]:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    for char in string:
        if char not in counts or counts[char] == 1:
            result += char
    return result