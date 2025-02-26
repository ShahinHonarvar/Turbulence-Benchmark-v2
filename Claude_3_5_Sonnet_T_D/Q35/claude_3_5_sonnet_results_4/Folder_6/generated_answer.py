def remove_repeat_chars(s):
    if len(s) <= 93:
        return s
    substring = s[21:93]
    char_count = {}
    for char in substring:
        char_count[char] = char_count.get(char, 0) + 1
    chars_to_remove = set((char for char, count in char_count.items() if count > 1))
    result = []
    for i, char in enumerate(s):
        if i < 21 or i >= 93 or char not in chars_to_remove:
            result.append(char)
    return ''.join(result)