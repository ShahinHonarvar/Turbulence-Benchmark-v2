def remove_repeat_chars(string):
    if len(string) <= 270:
        return string
    substring = string[71:200]
    char_counts = {}
    for char in substring:
        char_counts[char] = char_counts.get(char, 0) + 1
    chars_to_remove = set((char for char, count in char_counts.items() if count > 1))
    result = ''.join((char for char in string if char not in chars_to_remove))
    return result