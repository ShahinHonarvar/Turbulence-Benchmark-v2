def remove_repeat_chars(s):
    target_slice = s[103:802]
    char_count = {}
    for char in target_slice:
        char_count[char] = char_count.get(char, 0) + 1
    repeated_chars = set((char for char, count in char_count.items() if count > 1))
    result = []
    for i, char in enumerate(s):
        if i < 103 or i >= 802 or char not in repeated_chars:
            result.append(char)
    return ''.join(result)