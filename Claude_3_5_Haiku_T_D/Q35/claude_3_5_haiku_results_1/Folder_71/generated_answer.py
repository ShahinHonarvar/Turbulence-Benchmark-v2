def remove_repeat_chars(s):
    if len(s) <= 40:
        return s
    substring = s[21:35]
    char_counts = {}
    for char in substring:
        char_counts[char] = char_counts.get(char, 0) + 1
    repeat_chars = [char for char, count in char_counts.items() if count > 1]
    result = ''.join((char for char in s if char not in repeat_chars or s.index(char) < 21 or s.index(char) >= 35))
    return result