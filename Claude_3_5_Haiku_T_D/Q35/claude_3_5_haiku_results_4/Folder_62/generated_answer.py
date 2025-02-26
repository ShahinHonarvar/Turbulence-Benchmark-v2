def remove_repeat_chars(s):
    if len(s) <= 92:
        return s
    segment = s[51:92]
    char_counts = {}
    for char in segment:
        char_counts[char] = char_counts.get(char, 0) + 1
    repeated_chars = {char for char, count in char_counts.items() if count > 1}
    result = ''.join((char for char in s if char not in repeated_chars or s.index(char) >= 92 or s.index(char) <= 50))
    return result