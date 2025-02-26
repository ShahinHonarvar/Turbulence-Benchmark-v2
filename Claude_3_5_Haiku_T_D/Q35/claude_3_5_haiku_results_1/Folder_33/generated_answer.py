def remove_repeat_chars(s):
    if len(s) <= 250:
        return s
    substr = s[126:825]
    char_counts = {}
    for char in substr:
        char_counts[char] = char_counts.get(char, 0) + 1
    repeat_chars = set((char for char, count in char_counts.items() if count > 1))
    return ''.join((char for char in s if char not in repeat_chars or s.index(char) < 126 or s.index(char) >= 825))