def remove_repeat_chars(s):
    if len(s) <= 709:
        return s
    substring = s[477:709]
    char_counts = {}
    for char in substring:
        char_counts[char] = char_counts.get(char, 0) + 1
    repeat_chars = {char for char, count in char_counts.items() if count > 1}
    result = ''.join((char for char in s if char not in repeat_chars or s.index(char) <= 476 or s.index(char) >= 709))
    return result