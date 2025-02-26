def remove_repeat_chars(s):
    substring = s[476:709]
    char_count = {}
    for char in substring:
        char_count[char] = char_count.get(char, 0) + 1
    repeated_chars = set((char for char, count in char_count.items() if count > 1))
    result = []
    for i, char in enumerate(s):
        if i < 476 or i >= 709 or char not in repeated_chars:
            result.append(char)
    return ''.join(result)