def remove_repeat_chars(string):
    counts = {}
    for char in string[3:8]:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    unique_chars = ''
    for char in string:
        if char not in counts or counts[char] <= 1:
            unique_chars += char
    return unique_chars