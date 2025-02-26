def remove_repeat_chars(s):
    if len(s) <= 58:
        return s
    substring = s[58:85]
    char_counts = {}
    for char in substring:
        char_counts[char] = char_counts.get(char, 0) + 1
    repeated_chars = [char for char, count in char_counts.items() if count > 1]
    result = ''
    for char in s:
        if char not in repeated_chars or s.index(char) < 58 or s.index(char) >= 85:
            result += char
    return result