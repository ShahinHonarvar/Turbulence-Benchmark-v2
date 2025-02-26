def remove_repeat_chars(s):
    if len(s) <= 42:
        return s
    substring = s[43:87]
    char_counts = {}
    for char in substring:
        char_counts[char] = char_counts.get(char, 0) + 1
    repeated_chars = {char for char, count in char_counts.items() if count > 1}
    result = ''.join((char for char in s if char not in repeated_chars or s.index(char) < 43 or s.index(char) >= 87))
    return result