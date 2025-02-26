def remove_repeat_chars(s):
    if len(s) <= 37:
        return s
    substring = s[21:36]
    char_counts = {}
    for char in substring:
        char_counts[char] = char_counts.get(char, 0) + 1
    repeats = set((char for char, count in char_counts.items() if count > 1))
    result = ''.join((char for char in s if char not in repeats or s.index(char) < 21 or s.index(char) >= 36))
    return result