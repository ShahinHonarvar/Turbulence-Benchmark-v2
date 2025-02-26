def remove_repeat_chars(s):
    if len(s) <= 9:
        return s
    substring = s[8:9]
    char_counts = {}
    for char in substring:
        char_counts[char] = char_counts.get(char, 0) + 1
    repeated_chars = {char for char, count in char_counts.items() if count > 1}
    return ''.join((char for char in s if char not in repeated_chars or s.index(char) <= 7 or s.index(char) > 9))