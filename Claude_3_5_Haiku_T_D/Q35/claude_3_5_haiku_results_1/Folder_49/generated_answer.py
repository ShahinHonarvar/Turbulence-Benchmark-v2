def remove_repeat_chars(s):
    char_counts = {}
    for i in range(91, 200):
        if i < len(s):
            char = s[i]
            char_counts[char] = char_counts.get(char, 0) + 1
    repeated_chars = set((char for char, count in char_counts.items() if count > 1))
    return ''.join((char for char in s if char not in repeated_chars))