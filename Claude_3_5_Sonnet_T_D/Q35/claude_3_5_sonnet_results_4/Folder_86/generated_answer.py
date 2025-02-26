def remove_repeat_chars(s):
    substr = s[20:32]
    char_count = {}
    for char in substr:
        char_count[char] = char_count.get(char, 0) + 1
    repeat_chars = set((char for char, count in char_count.items() if count > 1))
    result = ''.join((char for char in s if char not in repeat_chars))
    return result