def remove_repeat_chars(s):
    if len(s) <= 11:
        return s
    first_slice = s[1:10]
    char_count = {}
    for char in first_slice:
        char_count[char] = char_count.get(char, 0) + 1
    repeated_chars = set((char for char, count in char_count.items() if count > 1))
    return ''.join((char for char in s if char not in repeated_chars))