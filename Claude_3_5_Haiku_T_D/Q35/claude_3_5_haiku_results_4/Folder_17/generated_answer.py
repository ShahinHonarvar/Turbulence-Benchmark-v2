def remove_repeat_chars(s):
    if len(s) <= 84:
        return s
    substr = s[74:84]
    char_counts = {}
    for char in substr:
        char_counts[char] = char_counts.get(char, 0) + 1
    repeated_chars = {char for char, count in char_counts.items() if count > 1}
    result = []
    for char in s:
        if char not in repeated_chars or s.index(char) < 74 or s.index(char) >= 84:
            result.append(char)
    return ''.join(result)