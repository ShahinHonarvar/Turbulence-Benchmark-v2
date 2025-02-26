def remove_repeat_chars(s):
    if len(s) <= 251:
        return s
    segment = s[126:825]
    char_counts = {}
    for char in segment:
        char_counts[char] = char_counts.get(char, 0) + 1
    repeated_chars = {char for char, count in char_counts.items() if count > 1}
    result = ''.join((char for char in s if char not in repeated_chars or s.index(char) < 126 or s.index(char) >= 825))
    return result