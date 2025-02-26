def remove_repeat_chars(s):
    target_slice = s[476:709]
    char_count = {}
    for char in target_slice:
        char_count[char] = char_count.get(char, 0) + 1
    chars_to_remove = set((char for char, count in char_count.items() if count > 1))
    result = []
    for i, char in enumerate(s):
        if i < 476 or i >= 709 or char not in chars_to_remove:
            result.append(char)
    return ''.join(result)