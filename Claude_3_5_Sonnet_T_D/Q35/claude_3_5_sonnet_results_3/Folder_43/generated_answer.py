def remove_repeat_chars(s):
    if len(s) <= 28:
        return s
    section = s[11:28]
    char_count = {}
    for char in section:
        char_count[char] = char_count.get(char, 0) + 1
    repeated_chars = set((char for char, count in char_count.items() if count > 1))
    result = []
    for i, char in enumerate(s):
        if char not in repeated_chars or (i < 11 or i >= 28):
            result.append(char)
    return ''.join(result)