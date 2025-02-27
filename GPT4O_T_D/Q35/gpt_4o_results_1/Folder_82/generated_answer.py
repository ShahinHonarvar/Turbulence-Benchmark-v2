def remove_repeat_chars(s):
    char_count = {}
    for i in range(31, min(200, len(s) - 1)):
        char = s[i]
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    chars_to_remove = set((char for char, count in char_count.items() if count > 1))
    result = []
    for char in s:
        if char not in chars_to_remove:
            result.append(char)
    return ''.join(result)