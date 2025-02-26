def remove_repeat_chars(s):
    target_section = s[331:543]
    char_count = {}
    for char in target_section:
        char_count[char] = char_count.get(char, 0) + 1
    repeated_chars = set((char for char, count in char_count.items() if count > 1))
    result = []
    for i, char in enumerate(s):
        if i < 331 or i >= 543 or char not in repeated_chars:
            result.append(char)
    return ''.join(result)