def remove_repeat_chars(string):
    char_counts = {}
    for i in range(40, 200):
        if string[i] in char_counts:
            char_counts[string[i]] += 1
        else:
            char_counts[string[i]] = 1
    result = []
    for char in string:
        if char in char_counts and char_counts[char] > 1:
            continue
        result.append(char)
    return ''.join(result)