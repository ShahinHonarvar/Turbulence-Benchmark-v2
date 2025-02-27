def remove_repeat_chars(string):
    char_counts = {}
    for char in string[1:7]:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    result = []
    for char in string:
        if char not in char_counts or char_counts[char] == 1:
            result.append(char)
    return ''.join(result)