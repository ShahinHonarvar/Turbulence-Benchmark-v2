def remove_repeat_chars(string):
    if len(string) <= 23:
        return string
    target_substring = string[23:24]
    char_counts = {}
    for char in target_substring:
        char_counts[char] = char_counts.get(char, 0) + 1
    chars_to_remove = set((char for char, count in char_counts.items() if count > 1))
    return ''.join((char for char in string if char not in chars_to_remove))