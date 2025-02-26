def remove_repeat_chars(s):
    if len(s) <= 30:
        return s
    substr = s[31:200]
    char_counts = {}
    for char in substr:
        char_counts[char] = char_counts.get(char, 0) + 1
    repeated_chars = {char for char, count in char_counts.items() if count > 1}
    result = ''.join((char for char in s if char not in repeated_chars or (s.index(char) < 31 or s.index(char) >= 200)))
    return result