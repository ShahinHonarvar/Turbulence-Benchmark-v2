def remove_repeat_chars(s):
    if len(s) <= 43:
        return s
    end = min(87, len(s))
    substring = s[43:end]
    char_counts = {}
    for char in substring:
        char_counts[char] = char_counts.get(char, 0) + 1
    repeated_chars = set((char for char, count in char_counts.items() if count > 1))
    result = []
    for i, char in enumerate(s):
        if i < 43 or i >= 87 or char not in repeated_chars:
            result.append(char)
    return ''.join(result)