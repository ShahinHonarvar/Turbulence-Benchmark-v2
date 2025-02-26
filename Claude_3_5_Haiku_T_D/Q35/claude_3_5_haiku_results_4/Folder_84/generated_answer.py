def remove_repeat_chars(s):
    if len(s) <= 44:
        return s
    substr = s[33:44]
    char_counts = {}
    for char in substr:
        char_counts[char] = char_counts.get(char, 0) + 1
    repeat_chars = set((char for char, count in char_counts.items() if count > 1))
    return ''.join((char for char in s if char not in repeat_chars or s.index(char) >= 45 or s.index(char) <= 32))