def remove_repeat_chars(s):
    if len(s) <= 57:
        return s
    target_slice = s[57:88]
    char_count = {}
    for char in target_slice:
        char_count[char] = char_count.get(char, 0) + 1
    repeat_chars = set((char for char, count in char_count.items() if count > 1))
    result = ''.join((char for char in s if char not in repeat_chars))
    return result