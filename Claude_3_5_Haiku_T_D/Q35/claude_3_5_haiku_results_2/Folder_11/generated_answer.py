def remove_repeat_chars(s):
    if len(s) <= 76:
        return s
    substring = s[49:76]
    char_count = {}
    for char in substring:
        char_count[char] = char_count.get(char, 0) + 1
    repeated_chars = set((char for char, count in char_count.items() if count > 1))
    result = ''.join((char for char in s if char not in repeated_chars or s.index(char) < 49 or s.index(char) >= 76))
    return result