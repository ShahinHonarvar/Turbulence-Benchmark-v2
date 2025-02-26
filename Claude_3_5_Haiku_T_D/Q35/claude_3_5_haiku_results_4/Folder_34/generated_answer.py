def remove_repeat_chars(s):
    if len(s) <= 70:
        return s
    substring = s[71:200]
    char_counts = {}
    for char in substring:
        char_counts[char] = char_counts.get(char, 0) + 1
    chars_to_remove = {char for char, count in char_counts.items() if count > 1}
    result = ''.join((char for char in s if char not in chars_to_remove or s.index(char) < 71 or s.index(char) >= 200))
    return result