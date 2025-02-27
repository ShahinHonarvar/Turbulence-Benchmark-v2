def remove_repeat_chars(string):
    char_counts = {}
    for i in range(33, 78):
        char = string[i]
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    result = []
    for char in string:
        if char in char_counts and char_counts[char] > 1:
            pass
        else:
            result.append(char)
    return ''.join(result)