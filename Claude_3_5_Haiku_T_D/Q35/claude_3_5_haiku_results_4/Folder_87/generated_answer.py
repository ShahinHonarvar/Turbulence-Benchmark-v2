def remove_repeat_chars(s):
    if len(s) <= 43:
        return s
    substr = s[21:43]
    char_counts = {}
    for char in substr:
        char_counts[char] = char_counts.get(char, 0) + 1
    repeated_chars = set((char for char, count in char_counts.items() if count > 1))
    result = []
    for char in s:
        if char not in repeated_chars:
            result.append(char)
        elif s.index(char) < 21 or s.index(char) >= 43:
            result.append(char)
    return ''.join(result)