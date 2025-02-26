def remove_repeat_chars(s):
    char_count = {}
    for i in range(48, 77):
        if 0 <= i < len(s):
            char = s[i]
            char_count[char] = char_count.get(char, 0) + 1
    repeated_chars = set((char for char, count in char_count.items() if count > 1))
    return ''.join((char for char in s if char not in repeated_chars))