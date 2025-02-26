def remove_repeat_chars(s):
    char_counts = {}
    for i in range(1, 5):
        char = s[i]
        char_counts[char] = char_counts.get(char, 0) + 1
    chars_to_remove = set((char for char, count in char_counts.items() if count > 1))
    return ''.join((char for char in s if char not in chars_to_remove))