def remove_repeat_chars(s):
    if len(s) <= 52:
        return s
    substr = s[51:76]
    char_count = {}
    for char in substr:
        char_count[char] = char_count.get(char, 0) + 1
    repeating_chars = set((char for char, count in char_count.items() if count > 1))
    result = []
    for i, char in enumerate(s):
        if i < 51 or i >= 76 or char not in repeating_chars:
            result.append(char)
    return ''.join(result)