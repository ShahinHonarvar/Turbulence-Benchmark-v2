def remove_repeat_chars(s):
    if len(s) <= 54:
        return s
    substr = s[30:53]
    char_counts = {}
    for char in substr:
        char_counts[char] = char_counts.get(char, 0) + 1
    repeated_chars = {char for char, count in char_counts.items() if count > 1}
    result = []
    for char in s:
        if char not in repeated_chars or s.index(char) > 53 or s.index(char) < 30:
            result.append(char)
    return ''.join(result)