def remove_repeat_chars(s):
    if len(s) <= 11:
        return s
    substring = s[11:76]
    char_counts = {}
    for char in substring:
        char_counts[char] = char_counts.get(char, 0) + 1
    repeated_chars = {char for char, count in char_counts.items() if count > 1}
    result = []
    for char in s:
        if char not in repeated_chars or (s.index(char) >= 11 and s.index(char) < 76):
            result.append(char)
    return ''.join(result)