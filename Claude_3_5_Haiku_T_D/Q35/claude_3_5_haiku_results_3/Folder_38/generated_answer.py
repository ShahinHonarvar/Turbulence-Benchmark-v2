def remove_repeat_chars(s):
    if len(s) <= 37:
        return s
    subset = s[37:85]
    char_counts = {}
    for char in subset:
        char_counts[char] = char_counts.get(char, 0) + 1
    repeat_chars = {char for char, count in char_counts.items() if count > 1}
    result = ''.join((char for char in s if char not in repeat_chars or s.index(char) < 37 or s.index(char) >= 85))
    return result